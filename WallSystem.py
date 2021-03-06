__author__ = 'Satha'
from Page import *
from Project import *
from Storage import *
from Comment import *

class WallSystem:
    def __init__(self, user):
        self.user = user
        self.history = [user]
        self.observers = []
        self.page = Page(self)
        self.notifyObservers()

    def addObserver(self,o):
        self.observers.append(o)

    def notifyObservers(self):
        for i in self.observers:
            i.updateObserver(self.user,self.history)

    def openProject(self,project):
        project.comments = Storage.getComments(project)
        self.history.append(project)
        self.notifyObservers()

    def addProject(self,name,tags,description):
        Storage.addProject(self.user.username,name,description)
        Storage.addProjectTags(self.user.username,name,tags)
        self.user.addProject(Project(self.user,name,description,tags))
        self.notifyObservers()

    def removeProject(self,project):
        while len(project.comments)!=0:
            self.removeComment(project,project.comments[0])
        self.editProjectTags(project,[])
        Storage.removeProject(self.user.username,project)
        self.user.removeProject(project)
        self.notifyObservers()

    def addComment(self,text):
        comment = Comment(self.user,text,len(self.history[-1].comments))
        self.history[-1].addComment(comment)
        Storage.addComment(self.history[-1],comment, self.user)

    def removeComment(self, project,comment):
        project.removeComment(comment)
        Storage.removeComment(project,comment)
        self.notifyObservers()

    def editUserTags(self,tags):
        self.user.tags = tags
        Storage.updateUserTag(self.user)
        self.notifyObservers()

    def editProjectTags(self,project,tags):
        project.tags = tags
        Storage.updateProjectTag(project)
        self.notifyObservers()

    def setPage(self, pageType, member, project=None):
        pass

    def fitText(self,label,width,height):
        textWidth = label.fontMetrics().boundingRect(label.text()).width()
        textHeight = label.fontMetrics().boundingRect(label.text()).height()
        label.resize(min(textWidth,width), min((textHeight,height)))

    def editProjectDescription(self,description):
        self.history[-1].description = description
        Storage.editProjectDescription(self.history[-1])
        self.notifyObservers()

    def goTo(self, item):
        self.history.append(item)
        self.notifyObservers()

    def changeProfilePhoto(self,filename):
        file = open(filename,'rb')
        binary = file.read()
        self.user.changeProfilePhoto(binary)
        Storage.changeProfilePhoto(self.user.username,binary)
        self.notifyObservers()

    def addProjectPhoto(self,filename):
        file = open(filename,'rb')
        binary = file.read()
        id = len(self.history[-1].photos)
        self.history[-1].addPhoto(binary)
        Storage.addProjectPhoto(self.history[-1],binary,id)
        self.notifyObservers()

    def removeProjectPhoto(self,photo):
        index = self.history[-1].getPhotoIndex(photo)
        self.history[-1].removePhoto(photo)
        Storage.removeProjectPhoto(self.history[-1],index)
        self.notifyObservers()