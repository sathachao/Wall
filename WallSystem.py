__author__ = 'Satha'
from Page import *
from Project import *
from Storage import *


class WallSystem:
    def __init__(self, user):
        self.user = user
        self.history = [user.wall]
        self.observers = []
        self.page = Page(self)
        self.notifyObservers()

    def addObserver(self,o):
        self.observers.append(o)

    def notifyObservers(self):
        for i in self.observers:
            i.updateObserver(self.user,self.history)

    def addProject(self,name,tags,description):
        Storage.addProject(self.user.username,name,description)
        Storage.addProjectTags(self.user.username,name,tags)
        self.user.wall.addProject(Project(name,tags,description))
        self.notifyObservers()

    def setPage(self, pageType, member, project=None):
        pass
