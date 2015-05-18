__author__ = 'Satha'

from PySide.QtGui import *
from PySide.QtCore import *
from PySide.QtUiTools import *
from ClickableLabel import *
from Member import *
from RegistrationPage import *
from WallSystem import *
import PopupDialog
import UI.loginPageRsc_rc
from Storage import *


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
        if Storage.checkLogin(username,password):
            user = Storage.getUser(username)
            self.system = WallSystem(user)
            self.hide()
        else:
            err = PopupDialog.PopupDialog("Wrong Password", self)

    def register(self):
        reg = RegistrationPage(self)