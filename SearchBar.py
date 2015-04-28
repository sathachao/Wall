__author__ = 'Satha'

from PySide.QtGui import *
from PySide.QtCore import *
from PySide.QtUiTools import *
from ClickableLabel import *
from SearchBox import *
import UI.searchBarRsc_rc


class SearchBar(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)

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

        self.connect(self.searchBtt, SIGNAL("clicked()"), self.getSearchResult)

        self.ui.show()

    def getSearchResult(self):
        x = self.searchBox.getItem()
        return self.searchBox.getItem()