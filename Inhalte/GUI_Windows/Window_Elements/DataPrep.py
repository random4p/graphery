from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QAbstractTableModel
from pandas import read_csv
from pandas import DataFrame
import numpy as np

DATA_SAMPLE = "../Sample_Files/apple.csv"
data = read_csv(DATA_SAMPLE, delimiter=",")
data = DataFrame.from_dict(data)


class DataPrep(QWidget):
    def __init__(self, parent, parent_2):
        super().__init__(parent)
        self.data = read_csv(DATA_SAMPLE)
        self.data_list = [self.data[i].values for i in data.keys()]
        self.table_widget = QTableWidget()

        self.create_table()

        parent.layout = QVBoxLayout()
        parent.layout.addWidget(self.table_widget)
        parent.setLayout(parent.layout)

    def create_table(self):
        self.table_widget.setRowCount(5)
        self.table_widget.setColumnCount(5)
        for i in self.data_list:
            for j in self.data_list[i]:
                self.table_widget.setItem(i, j, self.data_list[i][j])


keys = data.keys()
print(keys)
data_list = [data[i].values for i in keys]
print(data_list)
print(data_list[0][1])

for i in data_list:
    for j in range(3):
        print(data_list[i][j])





