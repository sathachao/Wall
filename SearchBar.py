__author__ = 'Satha'

from PySide.QtGui import *
from PySide.QtCore import *
from PySide.QtUiTools import *
from ClickableLabel import *
from SearchBox import *
import UI.searchBarRsc_rc
from WallObserver import *


class SearchBar(QWidget):
    def __init__(self, system,parent=None):
        QWidget.__init__(self, parent)
        self.system = system
        #self.system.addObserver(self)
        loader = QUiLoader()
        loader.registerCustomWidget(ClickableLabel)
        loader.registerCustomWidget(SearchBox)
        self.ui = loader.load("./UI/searchBar.ui", parent)
        self.backBtt = self.ui.findChild(ClickableLabel, "backBtt")
        self.homeBtt = self.ui.findChild(ClickableLabel, "homeBtt")
        self.searchBtt = self.ui.findChild(ClickableLabel, "searchBtt")
        self.settingBtt = self.ui.findChild(ClickableLabel, "settingBtt")
        self.nameLabel = self.ui.findChild(QLabel, "nameLabel")
        self.searchBox = self.ui.findChild(SearchBox, "searchBox")
        layout = QVBoxLayout(self)
        layout.addWidget(self.ui)
        layout.setContentsMargins(0, 0, 0, 0)

        self.connect(self.backBtt, SIGNAL("clicked()"),self.back)
        self.connect(self.searchBtt, SIGNAL("clicked()"),self.getItem)

    def back(self):
        if len(self.system.history) > 1:
            self.system.history.pop()
            self.system.notifyObservers()

    def getItem(self):
        item = self.searchBox.getItem()
        self.system.goTo(item)
