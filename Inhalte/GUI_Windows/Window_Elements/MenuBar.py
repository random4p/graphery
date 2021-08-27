from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class MakeMenuBar(QMainWindow):
    

    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        
        def make_menuBar(klasse):
            mainMenu = klasse.menuBar()
            fileMenu = mainMenu.addMenu('File')
            editMenu = mainMenu.addMenu('Edit')
            helpMenu = mainMenu.addMenu('Help')
                
            exitButton = QAction(QIcon('exit24.png'), 'Exit', klasse)
            exitButton.setShortcut('Ctrl+Q')
            exitButton.setStatusTip('Exit application')
            exitButton.triggered.connect(klasse.close)

            editButton = QAction(QIcon('back24.png'), 'Back', klasse)
            helpButton = QAction(QIcon('support24.png'), 'Support', klasse)
                
                
            fileMenu.addAction(exitButton)
            editMenu.addAction(editButton)
            helpMenu.addAction(helpButton)
            
            klasse.show()
        make_menuBar(parent)
        