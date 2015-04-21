__author__ = 'Satha'

from PySide.QtCore import *
from PySide.QtGui import *
from SearchBar import *
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SearchBar()
    sys.exit(app.exec_())