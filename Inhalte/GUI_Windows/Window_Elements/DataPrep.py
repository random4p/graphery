from PyQt5.QtGui import QFont, QPainter
from PyQt5.QtWidgets import *

# DATA_SAMPLE1 = "Sample_Files/apple.csv"
# data = read_csv(DATA_SAMPLE1, delimiter=",")
# data = DataFrame.from_dict(data)

# nominal: categorization into groups
# binary: yes or no
# ordinal: categorization - can be set into relation with other categories
# continuous/ ratio-scale: height, weight, time



type_of_data = ["binary", "nominal", "ordinal", "continuous/ratio-scale"]

class DataPrep:
    def __init__(self, parent, parent_2, data_set):
        self.data_set = data_set
        self.data_list = [self.data_set.data[i].values for i in self.data_set.data.keys()]
        self.parent = parent
        self.parent.layout = QGridLayout()

        # Boxes to better structure the GridLayout
        row_specification_layout = QGridLayout()
        settings_widget = QWidget()
        settings_widget.setMaximumHeight(230)
        settings_2_widget = QWidget()
        settings_2_widget.setMaximumHeight(200)
        settings_3_widget = QWidget()
        settings_3_widget.setMaximumHeight(200)

        # QComboBox to specify type of data
        self.specification_combo_box_list = []
        for i in range(len(self.data_set.data.keys())):
            specification_combo_box = QComboBox()
            specification_combo_box.addItem(f"{i+1}. Row")
            specification_combo_box.addItems(type_of_data)
            specification_combo_box.setMinimumSize(500, 50)
            self.specification_combo_box_list.append(specification_combo_box)
            row_specification_layout.addWidget(specification_combo_box, i+1, 0)

        # Label
        explanation_1 = QLabel("1. REQUIRED: Please specify the type of data for every row", settings_widget)
        explanation_1.setFont(QFont('Arial', 10))
        explanation_1.move(0, 80)
        explanation_1.setWordWrap(True)

        explanation_2 = QLabel(
            "2. It is possible to filter the data or to replace specific values with personalized ones: ",
            settings_2_widget)
        explanation_2.move(0, 80)
        explanation_2.setFont(QFont('Arial', 10))
        explanation_2.setWordWrap(True)

        explanation_3 = QLabel(
            "3. If you are done optimizing your data, you can confirm your changes by pushing the Apply-Button: ",
            settings_3_widget)
        explanation_3.move(0, 80)
        explanation_3.setFont(QFont('Arial', 10))
        explanation_3.setWordWrap(True)

        header = QLabel("Data-Optimization", settings_widget)
        header.setFont(QFont('Arial', 18))

        # button
        filter_button = QPushButton("Filter")
        filter_button.clicked.connect(lambda: self.filter_data())

        substitution_button = QPushButton("Substitute")
        substitution_button.clicked.connect(lambda: self.substitute_data())

        apply_button = QPushButton("Apply")
        apply_button.clicked.connect(lambda: self.confirm_changes())

        # create table with data
        self.parent.table_widget = QTableWidget()
        self.create_table()

        # add to the layout
        self.parent.layout.addWidget(self.parent.table_widget, 0, 0, 8, 1)
        self.parent.layout.addWidget(settings_widget, 0, 1)
        self.parent.layout.addLayout(row_specification_layout, 1, 1)
        self.parent.layout.addWidget(settings_2_widget, 2, 1)
        self.parent.layout.addWidget(filter_button, 3, 1)
        self.parent.layout.addWidget(substitution_button, 4, 1)
        self.parent.layout.addWidget(settings_3_widget, 5, 1)
        self.parent.layout.addWidget(apply_button, 6, 1)

        self.parent.setLayout(parent.layout)

    def create_table(self):
        self.parent.table_widget.setRowCount(self.data_set.data.shape[0])
        self.parent.table_widget.setColumnCount(self.data_set.data.shape[1])
        self.parent.table_widget.setHorizontalHeaderLabels(self.data_set.data.keys())
        for i in range(self.data_set.data.shape[1]):
            for j in range(self.data_set.data.shape[0]):
                self.parent.table_widget.setItem(j, i, QTableWidgetItem(f"{self.data_list[i][j]}"))

        for i in range(len(self.data_set.data.keys())):
            self.parent.table_widget.setColumnWidth(i, 250)

    def filter_data(self):
        for i in self.specification_combo_box_list:
            if "Row" in i.currentText():
                return
        self.filter_window = FilterPopup()
        self.filter_window.setGeometry(700, 700, 1000, 700)
        self.filter_window.show()


    def substitute_data(self):
        for i in self.specification_combo_box_list:
            if "Row" in i.currentText():
                return
        self.substitute_window = SubstituteWindow()
        self.substitute_window.setGeometry(700, 700, 1000, 700)
        self.substitute_window.show()

    def confirm_changes(self):
        pass


class FilterPopup(QWidget):
    def __init__(self):
        QWidget.__init__(self)

    def paintEvent(self, e):
        dc = QPainter(self)
        dc.drawLine(0, 0, 100, 100)
        dc.drawLine(100, 0, 0, 100)


class SubstituteWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)



