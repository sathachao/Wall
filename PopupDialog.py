__author__ = 'Satha'

from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtUiTools import *
from ClickableLabel import *
import UI.errorDialogRsc_rc
import sys

class PopupDialog(QWidget):
    def __init__(self, errorText, parent=None):
        QWidget.__init__(self, parent=parent)

        self.setWindowTitle("Wall")

        loader = QUiLoader()
        self.ui = loader.load("./UI/errorDialog.ui", self)

        self.errorTxt = self.ui.findChild(QLabel, "errorTxt")
        self.okayBtt = self.ui.findChild(ClickableLabel, "okayBtt")
        self.connect(self.okayBtt, SIGNAL("clicked()"), self.closeWindow)
        self.errorTxt.setText(errorText)
        self.ui.exec_()

    def closeWindow(self):
        self.ui.close()