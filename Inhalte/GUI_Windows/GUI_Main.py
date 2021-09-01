from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
# from DashTab import DashTab


import Inhalte.GUI_Windows.Window_Elements.DashTab
import Inhalte.GUI_Windows.Window_Elements.MenuBar 
#from Window_Elements.StyleSheet import Style
import Inhalte.GUI_Windows.Window_Elements.DataPrep
import Inhalte.GUI_Windows.Window_Elements.PlotTab


class Window(QMainWindow):

    def __init__(self, data_set):
    #def __init__(self):
        super().__init__()

        # this is the data manager object to be used --> give to the tabs to work with
        self.data_set = data_set

        # window configurations
        self.title = 'Graphery'
        self.setWindowTitle("Graphery")
        self.setGeometry(100, 60, 1000, 800)
        self.setWindowIcon(QIcon("Inhalte/GUI_Windows/Images/graphery_logo.png"))
        self.setMinimumSize(600, 500)
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 400
        self.showMaximized()
        Inhalte.GUI_Windows.Window_Elements.MenuBar.MakeMenuBar(self)

        # Style(self)

        self.table_widget = MyTableWidget(self, self.data_set)
        self.table_widget = MyTableWidget(self)
        self.setCentralWidget(self.table_widget)


class MyTableWidget(QWidget):

    def __init__(self, parent, data_set):
    #def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.data_set = data_set
        self.layout = QVBoxLayout(self)

        # Initialize tab screen
        self.tabs = QTabWidget()

        # create Tabs
        self.dash = QWidget()
        self.plot = QWidget()
        self.stat = QWidget()
        self.info = QWidget()
        self.data_prep = QWidget()
        self.tabs.resize(300, 200)

        # configure different tabs
        Inhalte.GUI_Windows.Window_Elements.DashTab.ConfigureDashTab(self.dash, self.tabs)
        Inhalte.GUI_Windows.Window_Elements.PlotTab.ConfigurePlotTab(self.plot)
        Inhalte.GUI_Windows.Window_Elements.DataPrep.DataPrep(self.data_prep, self.tabs, self.data_set)

        # Add specific tabs to tab-layout
        self.tabs.addTab(self.dash, "                    Dashboard                    ")
        self.tabs.addTab(self.plot, "                    Plot                    ")
        self.tabs.addTab(self.stat, "                    Statistics                    ")
        self.tabs.addTab(self.info, "                    Info                    ")
        self.tabs.addTab(self.data_prep, "                    Data Preparation                    ")

        # dont delete
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)
