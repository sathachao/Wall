__author__ = 'Faaiz'

from PySide.QtGui import *

class Project(QStandardItem):
    def __init__(self,owner,name,description="",tags=[],photos=[],sourcecode=[]):
        QStandardItem.__init__(self, name)
        self.wall = None
        self.tags = tags
        self.description = description
        self.name = name
        self.sourcecode = sourcecode
        self.photos = photos
        self.comments = []
        self.owner = owner

    def addComment(self,comment):
        self.comments.append(comment)

    def removeComment(self, comment):
        id = comment.id
        self.comments.remove(comment)
        while id!=len(self.comments):
            self.comments[id].id -= 1
            id += 1

    def addPhoto(self,photo):
        self.photos.append(photo)