
__author__ = 'Faaiz'
from PySide.QtUiTools import *
from PySide.QtGui import *
from PySide.QtCore import *

class ProjectCreateWidget(QDialog):
    def __init__(self,system):
        QDialog.__init__(self)
        self.setWindowFlags(Qt.CustomizeWindowHint)
        self.system = system
        self.loader = QUiLoader()
        self.dialog = self.loader.load("./UI/projectCreateDialog.ui")
        self.okBt = self.dialog.findChild(QPushButton,"okBt")
        self.removeBt = self.dialog.findChild(QPushButton,"removeBt")
        self.addBt = self.dialog.findChild(QPushButton,"addBt")
        self.cancelBt = self.dialog.findChild(QPushButton,"cancelBt")
        self.tagLine = self.dialog.findChild(QLineEdit,"tagLine")
        self.list = self.dialog.findChild(QListView,"list")
        self.projectNameLine = self.dialog.findChild(QLineEdit,"projectNameLine")
        self.descriptionText = self.dialog.findChild(QTextEdit,"descriptionText")
        self.sourcecodeLine = self.dialog.findChild(QLineEdit,"sourcecodeLine")
        self.photoLine = self.dialog.findChild(QLineEdit,"photoLine")
        self.scBrowseBt = self.dialog.findChild(QPushButton,"scBrowseBt")
        self.photoBrowseBt = self.dialog.findChild(QPushButton,"photoBrowseBt")
        layout = QVBoxLayout(self)
        layout.addWidget(self.dialog)
        self.cancelBt.clicked.connect(self.close)
        self.addBt.clicked.connect(self.add)
        self.removeBt.clicked.connect(self.remove)
        self.okBt.clicked.connect(self.confirm)
        self.model = QStandardItemModel(self.list)
        self.list.setModel(self.model)
        self.setModal(True)

    def confirm(self):
        tags = []
        for row in range(self.model.rowCount()):
            tags.append(self.model.item(row).text())
        name = self.projectNameLine.text()
        description = self.descriptionText.toPlainText()
        if name not in [project.name for project in self.system.user.wall.projects]:
            self.system.addProject(name,tags,description)
            self.close()

    def remove(self):
        self.model.takeRow(self.list.selectedIndexes()[0].row())

    def add(self):
        if self.tagLine.text() =="":
            return
        if len(self.model.findItems(self.tagLine.text()))==0:
            self.model.appendRow(QStandardItem(self.tagLine.text()))
            self.tagLine.setText("")


    def update(self, user):
        for tag in user.tags:
            self.model.appendRow((QStandardItem(tag)))


