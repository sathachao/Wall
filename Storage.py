__author__ = 'Faaiz'
import psycopg2
from Comment import *
from Member import *
from Project import *
from DatabaseManager import *
from SourceFile import *

class Storage():
    try:
        username = "wall_client"
        password = ""
        db = psycopg2.connect(database="Wall", user=username, password=password)
        db.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)
        cur = db.cursor()
        print("Connect successfully")
    except:
        print("Cannot connect to database")

#====================Methods for SignupPage

    @staticmethod
    def usernameExist(username):
        Storage.cur.execute("SELECT username FROM members WHERE username = %s", [username])
        if len(Storage.cur.fetchall()) == 0:
            return False
        return True

    @staticmethod
    def addMember(username,password,first,last):
        Storage.cur.execute("INSERT INTO members(username,password,firstname,lastname)"+
                         "VALUES(%s, %s, %s, %s, %s, %s)", [username, password, first, last])

#====================Methods for LoginPage
    @staticmethod
    def checkLogin(username,password):
        Storage.cur.execute("SELECT count(*) FROM members WHERE username = %s and password = %s",
                                [username, password])
        if Storage.cur.fetchall()[0][0] != 1:
            return False
        else:
            return True

    @staticmethod
    def getUserByName(first,last):
        Storage.cur.execute("SELECT username FROM members WHERE firstname = %s AND lastname = %s", [first, last])
        return Storage.getUser(Storage.cur.fetchall()[0][0])

    @staticmethod
    def getUser(username):
        Storage.cur.execute("SELECT * FROM members WHERE username = %s", [username])
        memberData = Storage.cur.fetchall()[0]
        Storage.cur.execute("SELECT tag FROM member_tags WHERE username = %s", [username])
        tags = Storage.cur.fetchall()
        for i in range(len(tags)):
            tags[i] = tags[i][0]
        member = Member(username=memberData[0],password=memberData[1],firstname=memberData[2],
                        lastname=memberData[3],tags=tags)
        member.projects = Storage.getProjects(member)
        return member

    @staticmethod
    def getProjects(member):
        Storage.cur.execute("SELECT proj_name FROM projects WHERE username = %s", [member.username])
        proj_names = Storage.cur.fetchall()
        projects = []
        for proj_name in proj_names:
            p = Storage.getProject(proj_name, member)
            p.comments = Storage.getComments(p)
            projects.append(p)
        return projects

    @staticmethod
    def getProject(projectName, member):
        Storage.cur.execute("SELECT * FROM projects WHERE proj_name = %s AND username = %s",
                                [projectName, member.username])
        data = Storage.cur.fetchall()
        if len(data) == 0:
            return None
        row = data[0]
        Storage.cur.execute("SELECT tag FROM project_tags WHERE proj_name = %s AND username = %s",
                                [projectName, member.username])
        tags = Storage.cur.fetchall()
        for i in range(len(tags)):
            tags[i] = tags[i][0]
        Storage.cur.execute("SELECT photo FROM project_photos WHERE proj_name = %s AND username = %s",
                                [projectName, member.username])
        photos = Storage.cur.fetchall()
        for i in range(len(photos)):
            photos[i] = photos[i][0].tobytes()
        return Project(member,row[0], row[1], tags,photos)

    @staticmethod
    def getComments(project):
        Storage.cur.execute("SELECT comment,id FROM project_comments WHERE proj_name = %s and username = %s",
                                [project.name, project.owner.username])
        comments = Storage.cur.fetchall()
        for i in range(len(comments)):
            comments[i] = Comment(project.owner, project,comments[i][0],int(comments[i][1]))
        return comments

    @staticmethod
    def updateUserTag(user):
        Storage.cur.execute("DELETE FROM member_tags WHERE username = %s" ,[user.username])
        for tag in user.tags:
            Storage.cur.execute("INSERT INTO member_tags(username,tag) VALUES(%s,%s)", [user.username, tag])

    @staticmethod
    def updateProjectTag(project):
        Storage.cur.execute("DELETE FROM project_tags WHERE username = %s AND proj_name = %s",
                                [project.owner.username, project.name])
        for tag in project.tags:
            Storage.cur.execute("INSERT INTO project_tags(username,proj_name,tag) VALUES(%s,%s,%s)"
                                    , [project.owner.username, project.name, tag])

    @staticmethod
    def addProject(username,name,description):
        Storage.cur.execute("INSERT INTO projects(username,proj_name,proj_description) VALUES(%s,%s,%s)"
                                , [username, name, description])

    @staticmethod
    def addProjectTags(username,name,tags):
        for tag in tags:
            Storage.cur.execute("INSERT INTO project_tags(username,proj_name,tag) VALUES(%s,%s,%s)"
                                    , [username, name,tag])

    @staticmethod
    def editProjectDescription(project):
        Storage.cur.execute("UPDATE projects SET proj_description = %s WHERE username = %s AND proj_name = %s",
                                [project.description,project.owner.username, project.name])

    @staticmethod
    def removeProject(username,project):
        for comment in project.comments:
            Storage.removeComment(project,comment)
        for tag in project.tags:
            Storage.removeProjectTag(project)
        Storage.cur.execute("DELETE FROM projects WHERE username = %s and proj_name = %s", [username, project.name])

    @staticmethod
    def addComment(project,comment):
        Storage.cur.execute("INSERT INTO project_comments(username,proj_name,comment,id) VALUES(%s,%s,%s,%s)",
                                [project.owner.username, project.name, comment.text,comment.id])

    @staticmethod
    def removeComment(project,comment):
        id = comment.id
        Storage.cur.execute("DELETE FROM project_comments WHERE username = %s and proj_name = %s and id = %s",
                                 [project.owner.username,project.name,comment.id])
        for i in range(len(project.comments)-id):
            Storage.cur.execute("UPDATE project_comments SET id = %s" +
                                    "WHERE username = %s AND proj_name = %s AND id = %s",
                                    [id + i , project.owner.username, project.name, id + i + 1])

    @staticmethod
    def addProjectPhoto(project,photo,id):
        binary = DatabaseManager.insertEscapeToBinary(photo)
        Storage.cur.execute("INSERT INTO project_photos(username,proj_name,photo,id) VALUES(%s,%s,%s,%s)",
                                [project.owner.username, project.name, binary, id])

#================Methods for SearchBox=====================

    @staticmethod
    def findUser(keyword):
        Storage.cur.execute("SELECT username FROM members WHERE lower(firstname) like concat(lower(%s),%s)",
                                [keyword, '%'])
        members = list()
        data = Storage.cur.fetchall()
        if len(data) == 0:
            return None
        for username in data:
            members.append(Storage.getUser(username))
        return members

    @staticmethod
    def findMemberWithTag(tag):
        Storage.cur.execute("SELECT username FROM members WHERE username in" +
                                "(SELECT username FROM member_tags WHERE lower(tag) = lower(%s))", [tag])
        members = list()
        for username in Storage.cur.fetchall():
            members.append(Storage.getUser(username))
        return members

    @staticmethod
    def findProject(keyword):
        Storage.cur.execute("SELECT proj_name, username FROM projects WHERE lower(proj_name) " +
                                "like concat(lower(%s),%s)", [keyword, '%'])
        projects = list()
        for proj_name, username in Storage.cur.fetchall():
            member = Storage.getUser(username)
            projects.append(Storage.getProject(proj_name, member))
        return projects

    @staticmethod
    def findProjectWithTag(tag):
        Storage.cur.execute("SELECT * FROM projects WHERE proj_name in" +
                                "(SELECT proj_name FROM project_tags WHERE lower(tag) = lower(%s))", [tag])
        projects = list()
        for project in Storage.cur.fetchall():
            member = Storage.getUser(project[2])
            projects.append(Storage.getProject(project[0], member))
        return projects

    @staticmethod
    def findItemsWithTag(tag):
        members = Storage.findMemberWithTag(tag)
        projects = Storage.findProjectWithTag(tag)
        items = list()
        for member in members:
            items.append(member)
        for project in projects:
            items.append(project)
        return items

#========================Source code methods========================
    @staticmethod
    def saveSourceFile(username, projectName, sourceFileName, sourceCode):
        try:
            Storage.cur.execute("INSERT INTO project_sourcecode(filename, sourcecode, username, proj_name) " +
                                    "VALUES(%s,%s,%s,%s)", [sourceFileName, sourceCode, username, projectName])
        except psycopg2.IntegrityError:
            print(sourceFileName, "already exists")

    @staticmethod
    def loadSourceFiles(username, projectName):
        Storage.cur.execute("SELECT filename, sourcecode FROM project_sourcecode " +
                                "WHERE username = %s and proj_name = %s", [username, projectName])
        sourceFiles = list()
        for filename, sourcecode in Storage.cur.fetchall():
            sourceFiles.append(SourceFile(filename, sourcecode))

        return sourceFiles

    @staticmethod
    def deleteSourceFile(username, projectName, sourceFileName):
        Storage.cur.execute("DELETE FROM project_sourcecode WHERE username = %s and proj_name = %s " +
                                "and filename = %s", [username, projectName, sourceFileName])
