__author__ = 'Faaiz'
from PySide.QtGui import *
from PySide.QtUiTools import *
from PySide.QtCore import *
from ClickableLabel import *
from WallObserver import *
from Project import *

class PhotoWidget(QWidget,WallObserver):
    def __init__(self,system,photo):
        QWidget.__init__(self)
        self.system = system
        self.system.addObserver(self)
        loader = QUiLoader()
        loader.registerCustomWidget(ClickableLabel)
        dialog = loader.load("./UI/photoWidget.ui")
        self.photo = photo
        self.picture = dialog.findChild(ClickableLabel,"picture")
        self.removeBt = dialog.findChild(QPushButton,"removeBt")
        self.image = QImage.fromData(photo)
        self.picture.setPixmap(QPixmap(self.image.scaled(90,90)))
        self.picture.setContentsMargins(0,0,0,0)

        self.connect(self.picture, SIGNAL("clicked()"),self.openPhoto)
        self.connect(self.removeBt,SIGNAL("clicked()"),self.removePhoto)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(0,0,0,0)
        layout.addWidget(dialog)

    def openPhoto(self):
        dialog = QDialog(self)
        layout = QVBoxLayout(dialog)
        label = QLabel()
        label.setPixmap(QPixmap(self.image))
        layout.addWidget(label)
        dialog.show()

    def removePhoto(self):
        self.system.removeProjectPhoto(self.photo)

    def updateObserver(self,user,history):
        if type(history[-1]) == Project:
            if history[-1].owner.username != user.username:
                self.removeBt.hide()
            else:
                self.removeBt.show()