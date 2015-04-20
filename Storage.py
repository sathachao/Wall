__author__ = 'Faaiz'
import psycopg2
from Member import *
from DatabaseManager import *

class Storage():

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
        DatabaseManager.execute("SELECT * FROM members WHERE username = '%s'" %(username))
        row = DatabaseManager.fetch()[0]
        DatabaseManager.execute("SELECT tag FROM member_tags WHERE username = '%s'" %(username))
        tags = DatabaseManager.fetch()
        for i in range(len(tags)):
            tags[i] = tags[i][0]
        return Member(row[0],row[1],row[2],row[3],tags=tags)

    @staticmethod
    def addMember(username,password,first,last,email):
        DatabaseManager.execute("INSERT INTO members(username,password,firstname,lastname,email)"+
                         "VALUES('%s', '%s', '%s', '%s', '%s', '%s')" %(username) %(password) %(first) %(last) %(email))

    @staticmethod
    def updateUserTag(user):
        DatabaseManager.execute("DELETE FROM member_tags WHERE username ='%s'" %(user.username))
        for tag in user.tags:
            DatabaseManager.execute("INSERT INTO member_tags(username,tag) VALUES('%s','%s')" %(user.username) %(tag))

    @staticmethod
    def addProject(username,name,description):
        DatabaseManager.execute("INSERT INTO projects(wallid,proj_name,proj_description) VALUES('%s','%s','%s')"
                                %(username) %(name) %(description))

    @staticmethod
    def addProjectTags(username,name,tags):
        for tag in tags:
            DatabaseManager.execute("INSERT INTO project_tags(username,proj_name,tag) VALUES('%s','%s','%s')"
                                    %(username) %(name) %(tag))
