from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class Style():

    def __init__(self, parent):
        super().__init__()
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
        # parent.setStyleSheet(css)