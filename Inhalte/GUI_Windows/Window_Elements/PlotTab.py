from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class ConfigurePlotTab(QWidget):

    def __init__(self, parent, parent_2):
        super(QWidget, self).__init__(parent)

        # add layout to plot
        parent.layout = QGridLayout()
        parent.layout.maximumSize()

        #create 2x2 matrix of layouts to be filled later with plot and settings
        dim_layout = QGridLayout()
        plot_layout = QGridLayout()
        specify_layout = QGridLayout()
        add_layout = QGridLayout()
        
        #configure dim_layout where the user will choose which data/ columns will be plotted

        #plot_tab is adding the 4 different layouts
        parent.layout.addLayout(dim_layout, 0, 0)
        parent.layout.addLayout(plot_layout, 0, 1)
        parent.layout.addLayout(specify_layout, 1, 0)
        parent.layout.addLayout(add_layout, 1, 1)
        

        parent.setLayout(parent.layout)