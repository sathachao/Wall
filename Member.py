__author__ = 'Satha'

from Wall import *


class Member():
    def __init__(self,wallId,firstname,lastname,username,password,email):
        self.wallId = wallId
        self.firstname = firstname
        self.lastname = lastname
        self.username = username
        self.password = password
        self.email = email
        self.tags = []
        self.wall = Wall(self)