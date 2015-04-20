__author__ = 'Faaiz'
from Wall import *


class Member():
    def __init__(self,username,password,firstname,lastname,tags):
        self.firstname = firstname
        self.lastname = lastname
        self.username = username
        self.password = password
        self.tags = tags
        self.wall = Wall(self)



