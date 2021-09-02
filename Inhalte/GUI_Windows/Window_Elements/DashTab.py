from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class ConfigureDashTab():

    def __init__(self, parent, parent_2):

        # add layout to dashboard
        parent.layout = QGridLayout()
        parent.layout.maximumSize()

        # input box with confirmation box for changing dimensions
        dash_rows = QSpinBox(parent)
        dash_rows.move(10, 20)
        dash_rows.resize(100, 40)

        dash_label_row = QLabel("Rows", parent)
        dash_label_row.setFont(QFont("Arial", 15))
        dash_label_row.move(112, 24)
        dash_label_row.setWordWrap(True)

        dash_cols = QSpinBox(parent)
        dash_cols.resize(100, 40)
        dash_cols.move(230, 20)

        dash_label_col = QLabel("Columns", parent)
        dash_label_col.setFont(QFont("Arial", 15))
        dash_label_col.move(330, 24)
        dash_label_col.setMinimumWidth(600)
        dash_label_col.setWordWrap(True)

        dash_confirm = QPushButton("Confirm", parent)
        dash_confirm.resize(230, 40)
        dash_confirm.move(500, 20)

        # messagebox if confirm button is clicked
        dash_confirm.clicked.connect(lambda: Warning_Window())

        def Warning_Window():
            reply = QMessageBox.question(parent, 'Change Dimensions',
                                         'Changing of dimensions leads to loss of plots and statistics. You have choosen {row} rows and {col} columns'.format(
                                             row=int(dash_rows.value()), col=int(dash_cols.value())),
                                         QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes:
                spin_method()
            else:
                pass

        def switch_window():
            pop_window = QMainWindow(parent)
            pop_window.setWindowTitle("Plot or Statistics")
            pop_window.setFixedSize(300, 130)
            CentralWidget = QWidget()
            CentralWidgetLayout = QHBoxLayout()
            plot_button = QPushButton("Plot")
            stat_button = QPushButton("Stat")
            CentralWidgetLayout.addWidget(plot_button)
            CentralWidgetLayout.addWidget(stat_button)
            CentralWidget.setLayout(CentralWidgetLayout)
            pop_window.setCentralWidget(CentralWidget)

            plot_button.clicked.connect(lambda: parent_2.setCurrentIndex(1))
            plot_button.clicked.connect(lambda: pop_window.close())
            stat_button.clicked.connect(lambda: parent_2.setCurrentIndex(2))
            stat_button.clicked.connect(lambda: pop_window.close())
            pop_window.show()

        # confirmation of dimension change box leads to creation of grid
        # maximum num of rows and columns is 6
        def spin_method():
            parent.list_of_buttons = []

            for i in range(int(dash_rows.value())):
                for j in range(int(dash_cols.value())):
                    plus = QPushButton("+")
                    plus.setFixedSize(QSize(30, 30))
                    parent.layout.addWidget(plus, i, j)
                    parent.list_of_buttons.append(plus)

            for button in parent.list_of_buttons:
                button.clicked.connect(lambda: switch_window())

        parent.setLayout(parent.layout)
