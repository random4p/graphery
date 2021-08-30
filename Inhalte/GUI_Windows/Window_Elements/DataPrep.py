from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QAbstractTableModel
from pandas import read_csv
import numpy

DATA_SAMPLE = "Inhalte/GUI_Windows/Sample_Files/apple.csv"
data = read_csv(DATA_SAMPLE)


class DataPrep(QWidget):
    def __init__(self, parent, parent_2):
        super().__init__(parent)
        self.data = read_csv(DATA_SAMPLE)

        table = TableCreator(self.data)
        view = QTableView()
        view.setModel(table)
        view.show()


class TableCreator(QAbstractTableModel):
    def __init__(self, raw_data):
        QAbstractTableModel.__init__(self)
        self.data = raw_data

    def rowCount(self, parent=None):
        return self.data.shape[0]

    def columnCount(self, parent=None):
        return self.data.shape[1]

    def data(self, index, role=Qt.DisplayRole):
        if index.isValid():
            if role == Qt.DisplayRole:
                return str(self.data.iloc(index.row(), index.column()))
        return None

    def headerData(self, section: int, orientation: Qt.Orientation, role: int = ...):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self.data.columns[section]
        return None







