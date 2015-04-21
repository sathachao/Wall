__author__ = 'Satha'


class Project:
    def __init__(self, projectName, projectDesc, username, tags):
        self.projectName = projectName
        self.projectDesc = projectDesc
        self.username = username
        self.tags = tags

    def getInfo(self):
        return [self.projectName, self.projectDesc, self.username, self.tags]