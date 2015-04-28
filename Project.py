__author__ = 'Faaiz'

from PySide.QtGui import *

class Project(QStandardItem):
    def __init__(self,name,description="",tags=[],sourcecode="",photo=[]):
        QStandardItem.__init__(self, name)
        self.wall = None
        self.tags = tags
        self.description = description
        self.name = name
        self.sourcecode = sourcecode
        self.photo = photo
        self.comments = []

    def addComment(self,comment):
        self.comments.append(comment)

    def removeComment(self, comment):
        id = comment.id
        self.comments.remove(comment)
        while id!=len(self.comments):
            self.comments[id].id -= 1
            id += 1