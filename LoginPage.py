__author__ = 'Satha'

from PySide.QtGui import *
from PySide.QtCore import *
from PySide.QtUiTools import *
from ClickableLabel import *
from DatabaseManager import *
import ErrorDialog
import UI.loginPageRsc_rc


class LoginPage(QWidget):
    def __init__(self, parent = None):
        QWidget.__init__(self, parent)
        self.setWindowTitle("Wall Authentication System")

        loader = QUiLoader()
        ui = loader.load("./UI/loginPage.ui", self)

        self.loginBtt = ui.findChild(QLabel, "loginBtt")
        clickable(self.loginBtt).connect(self.login)

        self.signupBtt = ui.findChild(QLabel, "signupBtt")
        self.usernameTxt = ui.findChild(QLineEdit, "usernameTxt")
        self.passwordTxt = ui.findChild(QLineEdit, "passwordTxt")

    def login(self):
        username = self.usernameTxt.text()
        password = self.passwordTxt.text()

        DatabaseManager.execute("SELECT username, password FROM members WHERE username = '%s';" %(username))

        outputList = DatabaseManager.fetch()
        print(username, password)
        print(outputList)
        if len(outputList) == 0:
            err = ErrorDialog.ErrorDialog("This username does not exist", self)
            err.show()
        elif username == outputList[0][0] and password == outputList[0][1]:
            print("Login successful")
        else:
            err = ErrorDialog.ErrorDialog("Wrong Password", self)
