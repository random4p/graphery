from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
#from DashTab import DashTab

import Inhalte.GUI_Windows.Window_Elements.DashTab
import Inhalte.GUI_Windows.Window_Elements.MenuBar 
 
#from Window_Elements.StyleSheet import Style

class Window(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.title = 'Graphery'
        self.setWindowTitle("Graphery")
        self.setGeometry(100, 60, 1000, 800)
        self.setWindowIcon(QIcon("Inhalte/GUI_Windows/Images/graphery_logo.png"))
        self.setMinimumSize(600, 500)
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 400
        Inhalte.GUI_Windows.Window_Elements.MenuBar.MakeMenuBar(self)
        

        #Style(self)

        self.table_widget = MyTableWidget(self)
        self.setCentralWidget(self.table_widget)
    

class MyTableWidget(QWidget):
    
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)
        
        # Initialize tab screen
        self.tabs = QTabWidget()
        
        #create Tabs
        self.dash = QWidget()
        self.plot = QWidget()
        self.stat = QWidget()
        self.info = QWidget()
        self.data_prep = QWidget()
        self.tabs.resize(300,200)

        #add attributes to tabs
        Inhalte.GUI_Windows.Window_Elements.DashTab.DashTab(self.dash, self.tabs)
        
        # Add specific tabs to tab-layout
        self.tabs.addTab(self.dash,"                    Dashboard                    ")
        self.tabs.addTab(self.plot,"                    Plot                    ")
        self.tabs.addTab(self.stat,"                    Statistics                    ")
        self.tabs.addTab(self.info,"                    Info                    ")
        self.tabs.addTab(self.data_prep,"                    Data Preparation                    ")

    
        #dont delete
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)    