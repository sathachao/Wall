__author__ = 'Faaiz'

from PySide.QtGui import *

class Member(QStandardItem):
    def __init__(self, firstname, lastname, username, password, tags,profilePhoto):
        QStandardItem.__init__(self, firstname + " " + lastname)
        self.firstname = firstname
        self.lastname = lastname
        self.username = username
        self.password = password
        self.tags = tags
        self.projects = []
        self.profilePhoto = profilePhoto

    def getInfo(self):
        return [self.firstname, self.lastname, self.username, self.password, self.tags]

    def __str__(self):
        return self.firstname + " " + self.lastname

    def text(self):
        return self.firstname + " " + self.lastname

    def addProject(self,p):
        self.projects.append(p)
        p.member = self

    def removeProject(self,p):
        for project in self.projects:
            if project.name == p.name:
                self.projects.remove(project)
                break

    def changeProfilePhoto(self,photo):
        self.profilePhoto = photo
