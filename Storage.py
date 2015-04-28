__author__ = 'Faaiz'
import psycopg2
from Comment import *
from Wall import *
from Member import *
from Project import *
from DatabaseManager import *
from Wall import *

class Storage():

#====================Methods for SignupPage
    @staticmethod
    def usernameExist(username):
        DatabaseManager.execute("SELECT username FROM members WHERE username = %s", [username])
        if len(DatabaseManager.fetch()) == 0:
            return False
        return True

    @staticmethod
    def addMember(username,password,first,last,email):
        DatabaseManager.execute("INSERT INTO members(username,password,firstname,lastname)"+
                         "VALUES(%s, %s, %s, %s, %s, %s)", [username, password, first, last])

#====================Methods for LoginPage
    @staticmethod
    def checkLogin(username,password):
        DatabaseManager.execute("SELECT count(*) FROM members WHERE username = %s and password = %s",
                                [username, password])
        if DatabaseManager.fetch()[0][0] != 1:
            return False
        else:
            return True

    @staticmethod
    def getUserByName(first,last):
        DatabaseManager.execute("SELECT username FROM members WHERE firstname = %s AND lastname = %s", [first, last])
        return Storage.getUser(DatabaseManager.fetch()[0][0])

    @staticmethod
    def getUser(username):
        DatabaseManager.execute("SELECT * FROM members WHERE username = %s", [username])
        memberData = DatabaseManager.fetch()[0]
        DatabaseManager.execute("SELECT tag FROM member_tags WHERE username = %s", [username])
        tags = DatabaseManager.fetch()
        for i in range(len(tags)):
            tags[i] = tags[i][0]
        member = Member(username=memberData[0],password=memberData[1],firstname=memberData[2],
                        lastname=memberData[3],tags=tags)
        member.wall = Storage.getWall(member)
        return member

    @staticmethod
    def getWall(member):
        wall = Wall(member, Storage.getProjects(member))
        for project in wall.projects:
            project.wall = wall
        return wall

    @staticmethod
    def getProjects(member):
        DatabaseManager.execute("SELECT proj_name FROM projects WHERE username = %s", [member.username])
        proj_names = DatabaseManager.fetch()
        projects = []
        for proj_name in proj_names:
            p = Storage.getProject(proj_name, member.username)
            p.comments = Storage.getComments(p, member)
            projects.append(p)
        return projects

    @staticmethod
    def getProject(projectName, username):
        DatabaseManager.execute("SELECT * FROM projects WHERE proj_name = %s and username = %s", [projectName, username])
        data = DatabaseManager.fetch()
        if len(data) == 0:
            return None
        row = data[0]
        DatabaseManager.execute("SELECT tag FROM project_tags WHERE proj_name = %s and username = %s", [projectName, username])
        tags = DatabaseManager.fetch()
        for i in range(len(tags)):
            tags[i] = tags[i][0]
        return Project(row[0], row[1], tags)

    @staticmethod
    def getComments(project,member):
        DatabaseManager.execute("SELECT comment,id FROM project_comments WHERE proj_name = %s and username = %s", [project.name, member.username])
        comments = DatabaseManager.fetch()
        for i in range(len(comments)):
            comments[i] = Comment(member, project,comments[i][0],int(comments[i][1]))
        return comments

    @staticmethod
    def updateUserTag(user):
        DatabaseManager.execute("DELETE FROM member_tags WHERE username = %s" ,[user.username])
        for tag in user.tags:
            DatabaseManager.execute("INSERT INTO member_tags(username,tag) VALUES(%s,%s)", [user.username, tag])

    @staticmethod
    def updateProjectTag(project):
        DatabaseManager.execute("DELETE FROM project_tags WHERE username = %s AND proj_name = %s",
                                [project.wall.owner.username, project.name])
        for tag in project.tags:
            DatabaseManager.execute("INSERT INTO project_tags(username,proj_name,tag) VALUES(%s,%s,%s)"
                                    , [project.wall.owner.username, project.name, tag])

    @staticmethod
    def addProject(username,name,description):
        DatabaseManager.execute("INSERT INTO projects(username,proj_name,proj_description) VALUES(%s,%s,%s)"
                                , [username, name, description])

    @staticmethod
    def addProjectTags(username,name,tags):
        for tag in tags:
            DatabaseManager.execute("INSERT INTO project_tags(username,proj_name,tag) VALUES(%s,%s,%s)"
                                    , [username, name,tag])

    @staticmethod
    def editProjectDescription(project):
        DatabaseManager.execute("UPDATE projects SET proj_description = %s WHERE username = %s AND proj_name = %s",
                                [project.description,project.wall.owner.username, project.name])

    @staticmethod
    def removeProject(username,project):
        for comment in project.comments:
            Storage.removeComment(project,comment)
        for tag in project.tags:
            Storage.removeProjectTag(project)
        DatabaseManager.execute("DELETE FROM projects WHERE username = %s and proj_name = %s", [username, project.name])

    @staticmethod
    def addComment(project,comment):
        DatabaseManager.execute("INSERT INTO project_comments(username,proj_name,comment,id) VALUES(%s,%s,%s,%s)",
                                [project.wall.owner.username, project.name, comment.text,comment.id])

    @staticmethod
    def removeComment(project,comment):
        id = comment.id
        DatabaseManager.execute("DELETE FROM project_comments WHERE username = %s and proj_name = %s and id = %s",
                                 [project.wall.owner.username,project.name,comment.id])
        for i in range(len(project.comments)-id):
            DatabaseManager.execute("UPDATE project_comments SET id = %s" +
                                    "WHERE username = %s AND proj_name = %s AND id = %s",
                                    [id + 1, project.wall.owner.username, project.name, id + 1])

#================Methods for SearchBox=====================

    @staticmethod
    def findUser(keyword):
        DatabaseManager.execute("SELECT username FROM members WHERE firstname like %s", [keyword+'%'])
        members = list()
        data = DatabaseManager.fetch()
        if len(data) == 0:
            return None
        for username in data:
            members.append(Storage.getUser(username))
        return members

    @staticmethod
    def findMemberWithTag(tag):
        DatabaseManager.execute("SELECT username FROM members WHERE username in" +
                                "(SELECT username FROM member_tags WHERE tag = %s)", [tag + '%'])
        members = list()
        for username in DatabaseManager.fetch():
            members.append(Storage.getUser(username))
        return members

    @staticmethod
    def findProject(keyword):
        DatabaseManager.execute("SELECT proj_name, username FROM projects WHERE proj_name like %s", [keyword + '%'])
        projects = list()
        for proj_name, username in DatabaseManager.fetch():
            projects.append(Storage.getProject(proj_name, username))
        return projects

    @staticmethod
    def findProjectWithTag(tag):
        DatabaseManager.execute("SELECT * FROM projects WHERE proj_name in" +
                                "(SELECT proj_name FROM project_tags WHERE tag = %s)", [tag])
        projects = list()
        for project in DatabaseManager.fetch():
            projects.append(Storage.getProject(project[0], project[2]))
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