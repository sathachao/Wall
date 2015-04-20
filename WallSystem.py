__author__ = 'Faaiz'
from Page import *


class WallSystem():
    def __init__(self,user):
        self.user = user
        self.directory = "WallPage"
        self.histroy = []
        self.page = Page()
        self.page.show()