__author__ = 'Faaiz'


class Member():
    def __init__(self, firstname, lastname, username, password, tags):
        self.firstname = firstname
        self.lastname = lastname
        self.username = username
        self.password = password
        self.tags = tags
        self.wall = None
    def getInfo(self):
        return [self.firstname, self.lastname, self.username, self.password, self.tags]

    def __str__(self):
        return self.firstname + " " + self.lastname
