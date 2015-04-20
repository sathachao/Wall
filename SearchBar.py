__author__ = 'Satha'

from PySide.QtGui import *
from PySide.QtCore import *
from PySide.QtUiTools import *
from ClickableLabel import *

class SearchBar(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)

        loader = QUiLoader()
        loader.registerCustomWidget(ClickableLabel)
        self.ui = loader.load("./UI/registerPage.ui", parent)
        self.backBtt = self.ui.findChild(ClickableLabel, "backBtt")
        self.homeBtt = self.ui.findChild(ClickableLabel, "homeBtt")
        self.searchBtt = self.ui.findChild(ClickableLabel, "searchBtt")
        self.settingBtt = self.ui.findChild(ClickableLabel, "settingBtt")
        self.nameLabel = self.ui.findChild(QLabel, "nameLabel")
        self.searchBox = self.ui.findChild(SearchBar, "searchBox")

