from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class ConfigurePlotTab(QWidget):

    def __init__(self, parent, parent_2):
        super(QWidget, self).__init__(parent)

        # add layout to dashboard
        parent.layout = QGridLayout()
        parent.layout.maximumSize()