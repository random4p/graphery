import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class MyTableWidget(QWidget):
    
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)
        
        # Initialize tab screen
        self.tabs = QTabWidget()
        self.dash = QWidget()
        self.plot = QWidget()
        self.stat = QWidget()
        self.info = QWidget()
        self.tabs.resize(300,200)
        
        # Add tabs
        self.tabs.addTab(self.dash,"Dashboard")
        self.tabs.addTab(self.plot,"Plot")
        self.tabs.addTab(self.stat,"Statistics")
        self.tabs.addTab(self.info,"Info")


        ########################
        #add layout to dashboard
        self.dash.layout = QGridLayout()
        self.dash.layout.maximumSize()


        #input box with confirmation box for changing dimensions
        self.dash_rows = QDoubleSpinBox(self.dash)
        self.dash_rows.move(10, 10)
        self.dash_label_row = QLabel("Rows", self.dash)
        self.dash_label_row.move(125, 10)
        self.dash_label_row.setWordWrap(True)
        self.dash_cols = QDoubleSpinBox(self.dash)
        self.dash_cols.move(200, 10)
        self.dash_label_col = QLabel("Columns", self.dash)
        self.dash_label_col.move(320, 10)
        self.dash_confirm = QPushButton("confirm", self.dash)
        self.dash_confirm.move(400, 10)
        
        #messagebox if confirm button is clicked
        self.dash_confirm.clicked.connect(lambda: Warning_Window())
        def Warning_Window():
            reply = QMessageBox.question(self, 'Change Dimensions', 
            'Changing of dimensions leads to loss of plots and statistics. You have choosen {row} rows and {col} columns'.format(row = int(self.dash_rows.value()), col = int(self.dash_cols.value())),
            QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes:
                spin_method()
            else:
                pass
        
        
        def switch_window():
            pop_window = QMainWindow(self)
            pop_window.setWindowTitle("Plot or Statistics")
            pop_window.setMinimumSize(300, 130)
            CentralWidget = QWidget()
            CentralWidgetLayout = QHBoxLayout()
            plot_button = QPushButton("Plot")
            stat_button = QPushButton("Stat")
            CentralWidgetLayout.addWidget(plot_button)
            CentralWidgetLayout.addWidget(stat_button)
            CentralWidget.setLayout(CentralWidgetLayout)
            pop_window.setCentralWidget(CentralWidget)
            
            plot_button.clicked.connect(lambda: self.tabs.setCurrentIndex(1))
            plot_button.clicked.connect(lambda: pop_window.close())
            stat_button.clicked.connect(lambda: self.tabs.setCurrentIndex(2))
            stat_button.clicked.connect(lambda: pop_window.close())
            pop_window.show()
    
        #confirmation of dimension change box leads to creation of grid
        #maximum num of rows and colums is 6
        def spin_method():
            self.list_of_buttons = []
            
            if int(self.dash_rows.value()) <= 6 and int(self.dash_cols.value()) <= 6:
                for i in range(int(self.dash_rows.value())):
                    for j in range(int(self.dash_cols.value())):
                            plus = QPushButton("+")
                            plus.setFixedSize(QSize(30, 30))
                            self.dash.layout.addWidget(plus,i, j)
                            self.list_of_buttons.append(plus)

            else:
                    reply = QMessageBox.question(self, 'Maximum Rows and Columns', 
                    'The maximum amount of rows and columns is 6. You haven choosen {row} rows and {col} columns'.format(row = int(self.dash_rows.value()), col = int(self.dash.cols.value())),
                    QMessageBox.Ok, QMessageBox.Ok)
                    if reply == QMessageBox.Ok:
                        pass
            for button in self.list_of_buttons:
                button.clicked.connect(lambda: switch_window())
                    
        self.dash.setLayout(self.dash.layout)
            
        
        ##############
        #plot tab
        
        
        
        
        #dont delete
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)