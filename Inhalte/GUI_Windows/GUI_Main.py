

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class Window(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.title = 'Graphery'
        self.setGeometry(100, 60, 1000, 800)
        self.setMinimumSize(600, 500)
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 400
        self.initUI()

        self.table_widget = MyTableWidget(self)
        self.setCentralWidget(self.table_widget)
    
    def initUI(self):
        
        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('File')
        editMenu = mainMenu.addMenu('Edit')
        helpMenu = mainMenu.addMenu('Help')
        
        exitButton = QAction(QIcon('exit24.png'), 'Exit', self)
        exitButton.setShortcut('Ctrl+Q')
        exitButton.setStatusTip('Exit application')
        exitButton.triggered.connect(self.close)

        editButton = QAction(QIcon('back24.png'), 'Back', self)
        helpButton = QAction(QIcon('support24.png'), 'Support', self)
        
        
        fileMenu.addAction(exitButton)
        editMenu.addAction(editButton)
        helpMenu.addAction(helpButton)
    
        self.show()

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
        
        #add layout to dashboard
        self.dash.layout = QGridLayout()
        self.dash.layout.maximumSize()
        # self.dash.layout.setColumnStretch(1, 4)
        # self.dash.layout.setColumnStretch(2, 4)
        #input box with confirmation box for changing dimensions
        self.dash.rows = QDoubleSpinBox(self.dash)
        self.dash.rows.move(10, 10)
        self.dash.label_row = QLabel("Rows", self.dash)
        self.dash.label_row.move(125, 10)
        self.dash.label_row.setWordWrap(True)
        self.dash.cols = QDoubleSpinBox(self.dash)
        self.dash.cols.move(200, 10)
        self.dash.label_col = QLabel("Columns", self.dash)
        self.dash.label_col.move(320, 10)
        self.dash.confirm = QPushButton("confirm", self.dash)
        self.dash.confirm.move(400, 10)
        
        #messagebox if confirm button is clicked
        self.dash.confirm.clicked.connect(lambda: Warning_Window())
        def Warning_Window():
            reply = QMessageBox.question(self, 'Change Dimensions', 
            'Changing of dimensions leads to loss of plots and statistics. You have choosen {row} rows and {col} columns'.format(row = int(self.dash.rows.value()), col = int(self.dash.cols.value())),
            QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes:
                spin_method()
            else:
                pass
        list_of_buttons = []
        #confirmation of dimension change box leads to creation of grid
        #maximum num of rows and colums is 6
        def spin_method():
            copy_list = list_of_buttons.copy()
            num_rows = int(self.dash.rows.value())
            num_col = int(self.dash.cols.value())
            if int(self.dash.rows.value()) <= 6:
                for i in range(num_rows):
                    for j in range(num_col):
                            plus = QPushButton("+")
                            plus.setFixedSize(QSize(30, 30))
                            self.dash.layout.addWidget(plus,i, j)
                            copy_list.append(plus)
            else:
                    reply = QMessageBox.question(self, 'Maximum Rows and Columns', 
                    'The maximum amount of rows and columns is 6. You haven choosen {row} rows and {col} columns'.format(row = int(self.dash.rows.value()), col = int(self.dash.cols.value())),
                    QMessageBox.Ok, QMessageBox.Ok)
                    if reply == QMessageBox.Ok:
                        pass

        self.dash.setLayout(self.dash.layout)
            
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)

    @pyqtSlot()
    def on_click(self):
        print("\n")
        for currentQTableWidgetItem in self.tableWidget.selectedItems():
            print(currentQTableWidgetItem.row(), currentQTableWidgetItem.column(), currentQTableWidgetItem.text())
    