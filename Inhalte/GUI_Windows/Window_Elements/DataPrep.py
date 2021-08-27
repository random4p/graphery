from PyQt5.QtWidgets import *
from PyQt5 import uic


class DataPrep(QWidget):
    def __init__(self, parent):
        super(DataPrep, self).__init__(parent)

        uic.loadUi("main_window_sample.ui", self)
        # self.btExport.clicked.connect(self.exportData)
        self.show()

        # parent.layout = QTableWidget()
        # parent.layout.maximumSize()
        #
        # self.button = QPushButton("parent", parent)
        # dash_confirm = QPushButton("confirm", parent)
        # dash_confirm.move(400, 10)
        #
        # parent.setLayout(parent.layout)


class TownsForm(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        uic.loadUi("main_window_sample.ui", self)
        # self.btExport.clicked.connect(self.exportData)
        self.show()


town = TownsForm()
