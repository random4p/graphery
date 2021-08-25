#In diese Datei kommen alle Imports und der Code für die Hauptdatei

import sys
from Inhalte.GUI_Windows.GUI_Main import Window
from PyQt5.QtWidgets import QApplication
from PyQt5 import *

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    ex = Window()
    sys.exit(app.exec_())