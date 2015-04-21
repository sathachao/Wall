__author__ = 'Faaiz'
from Page import *


class WallSystem():
    def __init__(self,user):
        self.user = user
        self.directory = "WallPage"
        self.history = ["WallPage"]
        self.observers = []
        self.page = Page(self)
        self.notifyObserver()

    def addObserver(self,o):
        self.observers.append(o)

    def notifyObserver(self):
        for i in self.observers:
            i.updateObserver(self.user,self.directory,self.history)
