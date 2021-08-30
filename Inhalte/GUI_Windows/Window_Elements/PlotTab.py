from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class ConfigurePlotTab(QWidget):

    def __init__(self, parent, parent_2):
        super(QWidget, self).__init__(parent)

        # add layout to dashboard
        parent.layout = QGridLayout()
        parent.layout.maximumSize()

        dim_layout = QGridLayout()
        plot_layout = QGridLayout()
        specify_layout = QGridLayout()
        add_layout = QGridLayout()
        #parent.addLayout(dim_layout)
        parent.layout.addLayout(dim_layout, 0, 0)
        parent.layout.addLayout(plot_layout, 0, 1)
        parent.layout.addLayout(specify_layout, 1, 0)
        parent.layout.addLayout(add_layout, 1, 1)
        #parent.layout.addWidget(dim_frame, 0, 0)

        parent.setLayout(parent.layout)