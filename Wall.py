__author__ = 'Faaiz'


class Wall:
    def __init__(self,owner,projects):
        self.owner = owner
        self.projects = projects

    def addProject(self,p):
        self.projects.append(p)
        p.wall = self

    def removeProject(self,p):
        self.projects.remove(p)