from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import *

# nominal: categorization into groups
# binary: yes or no
# ordinal: categorization - can be set into relation with other categories
# continuous/ ratio-scale: height, weight, time
type_of_data = ["binary", "nominal", "ordinal", "continuous/ratio-scale"]


# -----------------------------------------MAIN_DATAPREP_WINDOW------------------------------------------#
class DataPrep:
    def __init__(self, parent, parent_2, data_set):
        self.data_set = data_set
        self.parent = parent
        self.parent.layout = QGridLayout()

        # Boxes to better structure the GridLayout
        self.row_specification_layout = QGridLayout()
        settings_widget = QWidget()
        settings_widget.setMaximumHeight(230)
        settings_2_widget = QWidget()
        settings_2_widget.setMaximumHeight(200)
        settings_3_widget = QWidget()
        settings_3_widget.setMaximumHeight(200)

        # Boxes to specify the columns like described
        self.specification_combo_box_list = []
        for i in range(len(self.data_set.data.keys())):
            specification_combo_box = QComboBox()
            specification_combo_box.addItem(f"{i + 1}. Row")
            specification_combo_box.addItems(type_of_data)
            specification_combo_box.setMinimumSize(500, 50)
            specification_combo_box.show()
            self.specification_combo_box_list.append(specification_combo_box)
            self.row_specification_layout.addWidget(specification_combo_box, i + 1, 0)

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
        self.create_table()

        # add to the layout
        self.parent.layout.addWidget(settings_widget, 0, 1)
        self.parent.layout.addLayout(self.row_specification_layout, 1, 1)
        self.parent.layout.addWidget(settings_2_widget, 2, 1)
        self.parent.layout.addWidget(filter_button, 3, 1)
        self.parent.layout.addWidget(substitution_button, 4, 1)
        self.parent.layout.addWidget(settings_3_widget, 5, 1)
        self.parent.layout.addWidget(apply_button, 6, 1)

        self.parent.setLayout(parent.layout)

    def create_table(self):
        data_list = [self.data_set.data[i].values for i in self.data_set.data.keys()]
        self.table_widget = QTableWidget()
        self.table_widget.setRowCount(self.data_set.data.shape[0])
        self.table_widget.setColumnCount(self.data_set.data.shape[1])
        self.table_widget.setHorizontalHeaderLabels(self.data_set.data.keys())
        for i in range(self.data_set.data.shape[1]):
            for j in range(self.data_set.data.shape[0]):
                self.table_widget.setItem(j, i, QTableWidgetItem(f"{data_list[i][j]}"))

        for i in range(len(self.data_set.data.keys())):
            self.table_widget.setColumnWidth(i, 250)
        self.table_widget.show()
        self.parent.layout.addWidget(self.table_widget, 0, 0, 8, 1)

    def filter_data(self):
        self.filter_window = FilterPopup(self.data_set, self.create_table, self.table_widget)
        self.filter_window.setGeometry(700, 700, 1300, 700)
        self.filter_window.show()

    def substitute_data(self):
        self.substitute_window = SubstituteWindow(self.data_set, self.create_table, self.table_widget)
        self.substitute_window.setGeometry(700, 700, 600, 300)
        self.substitute_window.show()

    def confirm_changes(self):
        # list_column_spec = []
        # for i in self.specification_combo_box_list:
        #     if "Row" in i.currentText():
        #         return
        #     else:
        #         list_column_spec.append(i.currentText())

        self.ask_name = NameInputWindow(self.data_set)
        self.ask_name.setGeometry(700, 700, 600, 250)
        self.ask_name.show()


# ---------------------------------------FILTER_WINDOW-------------------------------------------#
class FilterPopup(QWidget):
    def __init__(self, data_set, create_table, table_widget):
        QWidget.__init__(self)
        self.setWindowTitle("Filter-Menu")
        self.data_set = data_set
        self.create_table = create_table
        self.table_widget = table_widget

        self.layout = QGridLayout()
        self.row_widget_list = []

        for i in range(len(self.data_set.data.keys())):
            row_widget = RowWidget(self.data_set.data.keys()[i])
            row_widget.show()
            self.layout.addWidget(row_widget, int(i / 4), i % 4)
            self.row_widget_list.append(row_widget)

        self.apply_button = QPushButton("Apply")
        self.apply_button.resize(300, 40)
        self.apply_button.clicked.connect(lambda: self.apply_changes())

        self.layout.addWidget(self.apply_button, int(len(self.data_set.data.keys()) / 4) + 2, 3)
        self.setLayout(self.layout)

    def apply_changes(self):
        for row_widget in self.row_widget_list:
            # all elements entered in a list will be filtered/excluded from the dataset
            # exceptions are still too broad !!!
            values = [value.strip() for value in row_widget.input_box.text().split(",")]
            for value in values:
                try:
                    index_value = self.data_set.data[self.data_set.data[row_widget.row] == int(value)].index
                    self.data_set.data = self.data_set.data.drop(index_value, axis=0)
                except:
                    try:
                        index_value = self.data_set.data[self.data_set.data[row_widget.row] == float(value)].index
                        self.data_set.data = self.data_set.data.drop(index_value, axis=0)
                    except:
                        index_value = self.data_set.data[self.data_set.data[row_widget.row] == value].index
                        self.data_set.data = self.data_set.data.drop(index_value, axis=0)
            # check box -> all values that are clicked will be removed from the dataset
            if row_widget.exclude_box.checkState():
                self.data_set.data = self.data_set.data.drop(f'{row_widget.row}', 1)

        self.create_table()
        self.table_widget.update()
        self.destroy()


# --------------------------------------SUBSTITUTION_WINDOW----------------------------------------#
class SubstituteWindow(QWidget):
    def __init__(self, data_set, create_table, table_widget):
        QWidget.__init__(self)
        self.data_set = data_set
        self.create_table = create_table
        self.table_widget = table_widget
        self.setWindowTitle("Substitution")
        label = QLabel("Please enter a value that you want to be changed and a value that will replace it: ", self)
        label.setFont(QFont("Arial", 12))
        label.move(80, 20)
        label.resize(500, 60)
        label.setWordWrap(True)

        self.replacee = QLineEdit(self)
        self.replacee.move(100, 80)
        self.replacee.resize(400, 40)

        self.replacer = QLineEdit(self)
        self.replacer.move(100, 120)
        self.replacer.resize(400, 40)

        replacee_label = QLabel("Old Value:", self)
        replacee_label.move(20, 86)
        replacer_label = QLabel("New Value:", self)
        replacer_label.move(20, 126)

        self.selection_box = QComboBox(parent=self)
        self.selection_box.addItems(["int", "float", "string"])
        self.selection_box.move(100, 160)
        self.selection_box.resize(200, 40)

        apply_button = QPushButton("Apply", self)
        apply_button.resize(300, 40)
        apply_button.move(280, 250)
        apply_button.clicked.connect(lambda: self.apply_changes())

    def apply_changes(self):
        if self.selection_box.currentText() == "int":
            self.data_set.data = self.data_set.data.replace(int(self.replacee.text()), int(self.replacer.text()))
        elif self.selection_box.currentText() == "float":
            self.data_set.data = self.data_set.data.replace(float(self.replacee.text()), float(self.replacer.text()))
        elif self.selection_box.currentText() == "string":
            self.data_set.data = self.data_set.data.replace(self.replacee.text().strip(), self.replacer.text().strip())

        self.create_table()
        self.table_widget.update()
        self.destroy()


# -----------------------------------------------HELPING_CLASSES--------------------------------------------#
class RowWidget(QWidget):
    def __init__(self, row):
        QWidget.__init__(self)

        self.row = row

        label = QLabel(f"{self.row}", self)
        label.setFont(QFont("Arial", 12))
        label.move(60, 20)
        label.setWordWrap(True)

        self.exclude_box = QCheckBox("Exclude column completely.", self)
        self.exclude_box.setFont(QFont("Arial", 9))
        self.exclude_box.move(20, 80)

        label2 = QLabel("Enter a list of values that will be filtered (separated with commas):", self)
        label2.setFont(QFont("Arial", 12))
        label2.setWordWrap(True)
        label2.setFont(QFont("Arial", 9))
        label2.move(20, 120)

        self.input_box = QLineEdit(self)
        self.input_box.move(20, 230)
        self.input_box.resize(400, 40)


class NameInputWindow(QWidget):
    def __init__(self, data_set):
        QWidget.__init__(self)

        self.name = data_set.name
        self.data_set = data_set

        new = QPushButton("Create new table", self)
        new.move(50, 70)
        new.resize(250, 40)
        new.clicked.connect(lambda: self.enable())

        change = QPushButton("Change existing table", self)
        change.move(300, 70)
        change.resize(250, 40)
        change.clicked.connect(lambda: self.confirm())

        self.name_input = QLineEdit(self)
        self.name_input.move(50, 120)
        self.name_input.resize(250, 40)
        self.name_input.setDisabled(True)

        self.confirm_input = QPushButton("Save", self)
        self.confirm_input.move(300, 120)
        self.confirm_input.resize(100, 40)
        self.confirm_input.setDisabled(True)
        self.confirm_input.clicked.connect(lambda: self.save())

    def enable(self):
        self.name_input.setEnabled(True)
        self.confirm_input.setEnabled(True)

    def confirm(self):
        self.data_set.create_new_sql_table(self.name)
        self.destroy()

    def save(self):
        self.name = self.name_input.text()
        self.data_set.create_new_sql_table(self.name)
        self.destroy()


