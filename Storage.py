__author__ = 'Faaiz'
import psycopg2
from Member import *
from Project import *
from DatabaseManager import *
from Wall import *

class Storage():

#====================Methods for SignupPage
    @staticmethod
    def checkSignup(username):
        DatabaseManager.execute("SELECT username FROM members WHERE username = '%s'" %(username))
        if len(DatabaseManager.fetch())==0:
            return True
        return False

    @staticmethod
    def addMember(username,password,first,last,email):
        DatabaseManager.execute("INSERT INTO members(username,password,firstname,lastname)"+
                         "VALUES('%s', '%s', '%s', '%s', '%s', '%s')" %(username) %(password) %(first) %(last))

#====================Methods for LoginPage
    @staticmethod
    def checkLogin(username,password):
        DatabaseManager.execute("SELECT count(*) FROM members WHERE username = '"+username+"' and password = '"+password+"'")
        if DatabaseManager.fetch()[0][0]!=1:
            return False
        else:
            return True

    @staticmethod
    def checkSignup(username):
        DatabaseManager.execute("SELECT username FROM members WHERE username = '%s'" %(username))
        if len(DatabaseManager.fetch())==0:
            return True
        return False

    @staticmethod
    def getUser(username):
        DatabaseManager.execute("SELECT * FROM members WHERE username = %s", [username])
        memberData = DatabaseManager.fetch()[0]
        DatabaseManager.execute("SELECT tag FROM member_tags WHERE username = %s", [username])
        tags = DatabaseManager.fetch()
        for i in range(len(tags)):
            tags[i] = tags[i][0]
        member = Member(username=memberData[0],password=memberData[1],firstname=memberData[2],lastname=memberData[3],tags=tags)
        wall = Wall(member,Storage.getProjects(username))
        member.wall = wall
        return member

    @staticmethod
    def getProjects(username):
        DatabaseManager.execute("SELECT * FROM projects WHERE username = '%s'"  %username)
        rows = DatabaseManager.fetch()
        projects = []
        for project in rows:
            DatabaseManager.execute("SELECT tag FROM project_tags WHERE proj_name = %s and username = %s", [project[0], username])
            tags = DatabaseManager.fetch()
            for i in range(len(tags)):
	            tags[i]=tags[i][0]
            projects.append(Project(project[0],tags,project[1]))
        return projects

    @staticmethod
    def getProject(projectName, username):
        DatabaseManager.execute("SELECT * FROM projects WHERE proj_name = %s and username = &s", [projectName, username])
        data = DatabaseManager.fetch()
        if len(data) == 0:
            return None
        row = data[0]
        DatabaseManager.execute("SELECT tag FROM project_tags WHERE proj_name = %s and username = &s", [projectName, username])
        tags = DatabaseManager.fetch()
        for i in range(len(tags)):
            tags[i] = tags[i][0]
        return Project(row[0], row[1], row[2], tags)

    @staticmethod
    def updateUserTag(user):
        DatabaseManager.execute("DELETE FROM member_tags WHERE username = %s" ,[user.username])
        for tag in user.tags:
            DatabaseManager.execute("INSERT INTO member_tags(username,tag) VALUES(%s,%s)" ,[user.username, tag])

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
    def removeProject(username,project):
        DatabaseManager.execute("DELETE FROM projects WHERE username = %s and proj_name = %s", [username, project.name])
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
                                "(SELECT username FROM member_tags WHERE tag = %s%)", [tag])
        members = list()
        for username in DatabaseManager.fetch():
            members.append(Storage.getUser(username))
        return members

    @staticmethod
    def findProject(keyword):
        DatabaseManager.execute("SELECT proj_name, username FROM projects WHERE proj_name like %s", [keyword+'%'])
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
