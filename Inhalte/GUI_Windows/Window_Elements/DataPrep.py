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
        self.parent.layout = QGridLayout()

        # to get more information of the row data
        row_specification_layout = QGridLayout()
        specifcation_label = QLabel("Column-Specification", parent)
        for i in range(len(self.data.keys())):
            specification_combo_box = QComboBox()
            specification_combo_box.setMinimumSize(350, 50)
            row_specification_layout.addWidget(specification_combo_box, i+1, 0)

        # button
        filter_button = QPushButton("Filter")
        substitution_button = QPushButton("Substitute")
        apply_button = QPushButton("Apply")

        # create table of data
        self.parent.table_widget = QTableWidget()
        self.create_table()

        # add to the layout
        self.parent.layout.addWidget(self.parent.table_widget, 0, 0, 5, 1)
        self.parent.layout.addLayout(row_specification_layout, 0, 1)
        self.parent.layout.addWidget(filter_button, 1, 1)
        self.parent.layout.addWidget(substitution_button, 2, 1)
        self.parent.layout.addWidget(apply_button, 4, 1)
        self.parent.setLayout(parent.layout)

    def create_table(self):
        self.parent.table_widget.setRowCount(self.data.shape[0]+1)
        self.parent.table_widget.setColumnCount(self.data.shape[1])
        self.parent.table_widget.setHorizontalHeaderLabels(self.data.keys())
        for i in range(self.data.shape[1]):
            for j in range(self.data.shape[0]):
                self.parent.table_widget.setItem(j, i, QTableWidgetItem(f"{self.data_list[i][j]}"))

        for i in range(len(self.data.keys())):
            self.parent.table_widget.setColumnWidth(i, 250)





