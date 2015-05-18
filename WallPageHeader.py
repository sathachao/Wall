__author__ = 'Faaiz'
from PySide.QtUiTools import *
from PySide.QtGui import *
from WallObserver import *
from Project import *
from Member import *
from PySide.QtCore import *

class WallPageHeader(QWidget,WallObserver):
    def __init__(self, system):
        QWidget.__init__(self,None)
        self.system = system
        self.system.addObserver(self)
        loader = QUiLoader()
        dialog = loader.load("./UI/wallPageHeader.ui")
        self.nameText = dialog.findChild(QLabel,"name")
        self.profilePhoto = dialog.findChild(QLabel,"profilePhoto")
        self.changePhotoBt = dialog.findChild(QPushButton,"changePhotoBt")
        layout = QVBoxLayout(self)
        layout.addWidget(dialog)

        layout.setContentsMargins(0,0,0,0)
        self.connect(self.changePhotoBt,SIGNAL("clicked()"),self.changeProfilePhoto)
        self.hide()

    def changeProfilePhoto(self):
        dialog = QFileDialog(self)
        dialog.setFileMode(QFileDialog.ExistingFile)
        dialog.setNameFilter("PNG Image (*.png)")
        if dialog.exec_():
            filename = dialog.selectedFiles()
            self.system.changeProfilePhoto(filename[0])

    def updateObserver(self,user,history):
        if type(history[-1]) == Member:
            self.nameText.setText(history[-1].firstname+" "+history[-1].lastname)
            self.system.fitText(self.nameText,430,40)
            if history[-1].username==self.system.user.username:
                self.changePhotoBt.show()
            else:
                self.changePhotoBt.hide()
            image = QImage.fromData(history[-1].profilePhoto)
            if image.height()!=0:
                factor = 159/image.height()
            else:
                factor = 0
            image = image.scaled(image.width()*factor, image.height()*factor)
            self.profilePhoto.setPixmap(QPixmap.fromImage(image))
            self.show()
        else:
            self.hide()


