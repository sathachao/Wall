__author__ = 'Faaiz'
from PySide.QtUiTools import *
from PySide.QtGui import *
from PySide.QtCore import *
from  WallObserver import *
from Project import *


class CommentWidget(QWidget,WallObserver):
    def __init__(self,comment,system):
        QWidget.__init__(self,None)
        loader = QUiLoader()
        dialog = loader.load("./UI/commentWidget.ui")
        self.system = system
        self.system.addObserver(self)
        self.comment = comment
        self.nameLabel = dialog.findChild(QLabel,"nameLabel")
        self.commentText = dialog.findChild(QPlainTextEdit,"commentText")
        self.removeBt = dialog.findChild(QPushButton,"removeBt")
        self.nameLabel.setText(self.comment.commenter.firstname+" "+self.comment.commenter.lastname)
        self.commentText.setPlainText(self.comment.text)
        layout = QVBoxLayout(self)
        layout.addWidget(dialog)
        layout.setContentsMargins(0,0,0,0)
        self.connect(self.removeBt,SIGNAL("clicked()"),self.remove)
        self.removeBt.hide()

    def remove(self):
        self.system.removeComment(self.system.history[-1],self.comment)

    def updateObserver(self,user,history):
        if type(history[-1]) == Project:
            if user.username == history[-1].owner.username or user.username == self.comment.commenter:
                self.removeBt.show()
            else:
                self.removeBt.hide()