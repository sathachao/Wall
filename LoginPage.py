__author__ = 'Satha'

from PySide.QtGui import *
from PySide.QtCore import *
from PySide.QtUiTools import *
from ClickableLabel import *
from DatabaseManager import *
from RegistrationPage import *
import ErrorDialog
import UI.loginPageRsc_rc


class LoginPage(QWidget):
    def __init__(self, parent = None):
        QWidget.__init__(self, parent)
        self.setWindowTitle("Wall Authentication System")

        loader = QUiLoader()
        loader.registerCustomWidget(ClickableLabel)
        print(loader.availableWidgets())

        ui = loader.load("./UI/loginPage.ui", self)

        self.loginBtt = ui.findChild(QLabel, "loginBtt")
        self.signupBtt = ui.findChild(QLabel, "signupBtt")
        self.usernameTxt = ui.findChild(QLineEdit, "usernameTxt")
        self.passwordTxt = ui.findChild(QLineEdit, "passwordTxt")

        self.connect(self.loginBtt, SIGNAL("clicked()"), self.login)
        self.connect(self.signupBtt, SIGNAL("clicked()"), self.register)

    def login(self):
        username = self.usernameTxt.text()
        password = self.passwordTxt.text()

        DatabaseManager.execute("SELECT username, password FROM members WHERE username = '%s';" %(username))

        outputList = DatabaseManager.fetch()
        print(username, password)
        print(outputList)
        if len(outputList) == 0:
            err = ErrorDialog.ErrorDialog("This username does not exist", self)
        elif username == outputList[0][0] and password == outputList[0][1]:
            print("Login successful")
        else:
            err = ErrorDialog.ErrorDialog("Wrong Password", self)

    def register(self):
        reg = RegistrationPage(self)