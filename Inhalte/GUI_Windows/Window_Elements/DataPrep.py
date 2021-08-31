from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QAbstractTableModel
from pandas import read_csv
from pandas import DataFrame

DATA_SAMPLE1 = "Inhalte/GUI_Windows/Sample_Files/apple.csv"
data = read_csv(DATA_SAMPLE1, delimiter=",")
data = DataFrame.from_dict(data)


class DataPrep:
    def __init__(self, parent, parent_2):
        self.data = read_csv(DATA_SAMPLE1)
        self.data_list = [self.data[i].values for i in data.keys()]
        self.parent = parent
        self.parent.table_widget = QTableWidget()

        self.create_table()

        self.parent.layout = QVBoxLayout()
        self.parent.layout.addWidget(parent.table_widget)
        self.parent.setLayout(parent.layout)

    def create_table(self):
        self.parent.table_widget.setRowCount(self.data.shape[0]+1)
        self.parent.table_widget.setColumnCount(self.data.shape[1])
        for i in range(len(self.data.keys())):
            self.parent.table_widget.setItem(0, i, QTableWidgetItem(self.data.keys()[i]))
        for i in range(self.data.shape[1]):
            for j in range(self.data.shape[0]):
                self.parent.table_widget.setItem(j+1, i, QTableWidgetItem(f"{self.data_list[i][j]}"))






