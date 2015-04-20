__author__ = 'Faaiz'


class Member():
    def __init__(self, firstname, lastname, username, password, email):
        self.firstname = firstname
        self.lastname = lastname
        self.username = username
        self.password = password
        self.email = email

    def getInfo(self):
        return [self.firstname, self.lastname, self.username, self.password, self.email]