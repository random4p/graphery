#In diese Datei kommen alle Imports und der Code für die Hauptdatei
# from tkinter import *
# from Inhalte.GUI_Windows.GUI_Ersatz import Window

import sys
from Inhalte.GUI_Windows.GUI_qt_Main import Window
from PyQt5.QtWidgets import (
    QApplication,
    QCheckBox,
    QTabWidget,
    QVBoxLayout,
    QWidget,
)
from PyQt5.QtGui import QPalette
from PyQt5.QtCore import Qt

#creates GUI and executes it
# root = Window()
# root.start()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    qp = QPalette()
    qp.setColor(QPalette.ButtonText, Qt.black)
    qp.setColor(QPalette.Window, Qt.black)
    qp.setColor(QPalette.Button, Qt.gray)
    app.setPalette(qp)
    window = Window()
    window.show()
    sys.exit(app.exec_())