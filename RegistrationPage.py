__author__ = 'Satha'

from PySide.QtGui import *
from PySide.QtCore import *
from PySide.QtUiTools import *
from ClickableLabel import *
import UI.registerPageRsc_rc
from Storage import *
from ErrorDialog import *


class RegistrationPage(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent=parent)

        loader = QUiLoader()
        loader.registerCustomWidget(ClickableLabel)
        self.ui = loader.load("./UI/registerPage.ui", self)

        self.ui.setWindowTitle("Registration Page")

        self.firstnameTxt = self.ui.findChild(QLineEdit, "firstnameTxt")
        self.lastnameTxt = self.ui.findChild(QLineEdit, "lastnameTxt")
        self.usernameTxt = self.ui.findChild(QLineEdit, "usernameTxt")
        self.passwordTxt = self.ui.findChild(QLineEdit, "passwordTxt")
        self.confirmTxt = self.ui.findChild(QLineEdit, "confirmTxt")

        self.registerBtt = self.ui.findChild(ClickableLabel, "registerBtt")

        self.connect(self.registerBtt, SIGNAL("clicked()"), self.register)

        self.ui.exec()


    def register(self):
        #List[firstname,lastname,username,password,confirmPW,email]

        valid = True
        data = [self.firstnameTxt.text(), self.lastnameTxt.text(), self.usernameTxt.text(),
                self.passwordTxt.text(), self.confirmTxt.text()]

        if Storage.usernameExist(self.usernameTxt.text()):
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
            DatabaseManager.execute("INSERT INTO members(username,password,firstname,lastname) VALUES(%s, %s, %s, %s);",
                                    [data[2],data[3],data[0],data[1]])
            errText = "Registration successful"

        err = ErrorDialog(errText, self)
        if valid == True:
            self.ui.close()