__author__ = 'Faaiz'


class Project():
    def __init__(self,name,tags=[],description="",sourcecode="",photo=[]):
        self.tags = tags
        self.description = description
        self.name = name
        self.sourcecode = sourcecode
        self.photo = photo
