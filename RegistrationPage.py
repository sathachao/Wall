__author__ = 'Satha'

from PySide.QtGui import *
from PySide.QtCore import *
from PySide.QtUiTools import *
from ClickableLabel import *
import UI.registerPageRsc_rc


class RegistrationPage(QWidget):
    def __init__(self, errorText, parent=None):
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
        self.errorTxt.setText(errorText)
        self.ui.exec_()

    def register(self):
        #List[firstname,lastname,username,password,confirmPW,email]



        firstname = self.firstnameTxt.text()
        lastname = self.lastnameTxt.text()
        username = self.usernameTxt.text()
        password = self.passwordTxt.text()
        confirmTxt = self.confirmTxt.text()
        email = self.emailTxt.text()


