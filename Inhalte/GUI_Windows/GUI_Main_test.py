from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from GUI_DashTabs import DashTab


class Window(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'Graphery'
        self.setWindowTitle("Graphery")
        self.setGeometry(100, 60, 1000, 800)
        self.setMinimumSize(600, 500)
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 400
        self.make_menuBar()
        self.setWindowIcon(QIcon("Inhalte/GUI_Windows/Images/graphery_logo.png"))

        # css = """
        # QWidget{
        #     Background: white;
        #     color:white;
        #     font:12px bold;
        #     font-weight:bold;
        #     border-radius: 1px;
        #     height: 11px;
        # }
        # QDialog{
        #     Background-image:url('img/titlebar bg.png');
        #     font-size:12px;
        #     color: black;

        # }
        # QToolButton{
        #     Background:#AA00AA;
        #     font-size:11px;
        # }
        # QToolButton:hover{
        #     Background: #FF00FF;
        #     font-size:11px;
        # }
        # """
        # self.setStyleSheet(css)

        self.table_widget = MyTableWidget(self)
        self.setCentralWidget(self.table_widget)

    def make_menuBar(self):
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

        # create Tabs and add specifics
        self.dash = QWidget()
        DashTab(self.dash, self.tabs)
        self.plot = QWidget()
        self.stat = QWidget()
        self.info = QWidget()
        self.tabs.resize(300, 200)

        # Add specific tabs to tab-layout
        self.tabs.addTab(self.dash, "Dashboard")
        self.tabs.addTab(self.plot, "Plot")
        self.tabs.addTab(self.stat, "Statistics")
        self.tabs.addTab(self.info, "Info")

        # dont delete
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)

    # @pyqtSlot()
    # def on_click(self):
    #     print("\n")
    #     for currentQTableWidgetItem in self.tableWidget.selectedItems():
    #         print(currentQTableWidgetItem.row(), currentQTableWidgetItem.column(), currentQTableWidgetItem.text())
