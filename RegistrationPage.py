__author__ = 'Satha'

from PySide.QtGui import *
from PySide.QtCore import *
from PySide.QtUiTools import *
from ClickableLabel import *
import UI.registerPageRsc_rc
from DatabaseManager import *
from ErrorDialog import *


class RegistrationPage(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent=parent)

        self.setWindowTitle("Registration Page")

        loader = QUiLoader()
        self.ui = loader.load("./UI/registerPage.ui", self)

        self.firstnameTxt = self.ui.findChild(QLineEdit, "firstnameTxt")
        self.lastnameTxt = self.ui.findChild(QLineEdit, "lastnameTxt")
        self.usernameTxt = self.ui.findChild(QLineEdit, "usernameTxt")
        self.passwordTxt = self.ui.findChild(QLineEdit, "passwordTxt")
        self.confirmTxt = self.ui.findChild(QLineEdit, "confirmTxt")
        self.emailTxt = self.ui.findChild(QLineEdit, "emailTxt")
        self.registerBtt = self.ui.findChild(QLabel, "registerBtt")

        clickable(self.registerBtt).connect(self.register)
        self.ui.exec_()

    def register(self):
        #List[firstname,lastname,username,password,confirmPW,email]

        valid = True
        data = [self.firstnameTxt.text(), self.lastnameTxt.text(), self.usernameTxt.text(),
                self.passwordTxt.text(), self.confirmTxt.text(), self.emailTxt.text()]

        DatabaseManager.execute("SELECT username FROM members WHERE username = '%s';" %(data[2]))

        if len(DatabaseManager.fetch()) > 0:
            valid = False
            errText = "This username already exists"

        elif len(data[3]) < 8:
            valid = False
            errText = "Password must be at least 8 characters long"

        elif data.count("") > 0:
            valid = False
            errText = "Please fill in every box"

        elif data[3] != data[4]:
            valid = False
            errText = "Password does not match\nwith confirmation password"

        if valid == True:
            DatabaseManager.execute("SELECT count(*) FROM members")
            wallID = DatabaseManager.fetch()[0][0]
            DatabaseManager.execute("INSERT INTO members(username,password,firstname,lastname,email,wallid) VALUES(%s, %s, %s, %s, %s,%s);",
                                    [data[2],data[3],data[0],data[1],data[5],wallID])
            errText = "Registration successful"

        err = ErrorDialog(errText, self)
        if valid == True:
            self.ui.close()