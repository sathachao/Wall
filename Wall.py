__author__ = 'Faaiz'


class Wall:
    def __init__(self,owner):
        self.owner = owner
        self.projects = []

    def addProject(self,p):
        self.projects.append(p)