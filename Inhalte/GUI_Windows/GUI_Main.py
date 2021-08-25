import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QVBoxLayout, QTabWidget, QAction, QHBoxLayout, QGroupBox, QDialog, QGridLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

class Window(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.title = 'Graphery'
        self.setGeometry(100, 60, 1000, 800)
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
        
        
        
        self.dash.layout = QGridLayout()
        self.dash.layout.setColumnStretch(1, 4)
        self.dash.layout.setColumnStretch(2, 4) 
        self.dash.layout.addWidget(QPushButton('1'),0,0)
        self.dash.layout.addWidget(QPushButton('2'),0,1)
        self.dash.layout.addWidget(QPushButton('3'),0,2)
        self.dash.layout.addWidget(QPushButton('4'),1,0)
        self.dash.layout.addWidget(QPushButton('5'),1,1)
        self.dash.layout.addWidget(QPushButton('6'),1,2)
        self.dash.layout.addWidget(QPushButton('7'),2,0)
        self.dash.layout.addWidget(QPushButton('8'),2,1)
        self.dash.setLayout(self.dash.layout)
        
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)

    @pyqtSlot()
    def on_click(self):
        print("\n")
        for currentQTableWidgetItem in self.tableWidget.selectedItems():
            print(currentQTableWidgetItem.row(), currentQTableWidgetItem.column(), currentQTableWidgetItem.text())
    