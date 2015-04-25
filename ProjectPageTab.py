__author__ = 'Faaiz'
from PySide.QtUiTools import *
from PySide.QtGui import *
from WallObserver import *
from Project import *
from Wall import *
from UI.ProjectPageTabRsc_rc import *
from ClickableLabel import *

class ProjectPageTab(QWidget,WallObserver):
    def __init__(self,system,content):
        QWidget.__init__(self,None)
        self.system = system
        self.content = content
        self.system.addObserver(self)
        loader = QUiLoader()
        loader.registerCustomWidget(ClickableLabel)
        layout = QVBoxLayout()
        dialog = loader.load("./UI/projectPageTab.ui")
        self.descriptionBt = dialog.findChild(ClickableLabel,"descriptionLabel")
        self.commentsBt = dialog.findChild(ClickableLabel,"commentsLabel")
        self.photosBt = dialog.findChild(ClickableLabel,"photosLabel")
        self.sourcecodeBt = dialog.findChild(ClickableLabel,"sourcecodeLabel")
        self.connect(self.descriptionBt,SIGNAL("clicked()"),self.content.openDescriptionTab)
        self.connect(self.commentsBt,SIGNAL("clicked()"),self.content.openCommentTab)
        self.connect(self.photosBt,SIGNAL("clicked()"),self.content.openPhotoTab)
        self.connect(self.sourcecodeBt,SIGNAL("clicked()"),self.content.openSourcecodeTab)
        layout.addWidget(dialog)
        layout.setContentsMargins(0,0,0,0)
        self.setLayout(layout)
        self.hide()

    def updateObserver(self,user,history):
        if type(history[-1]) == Project:
            self.show()