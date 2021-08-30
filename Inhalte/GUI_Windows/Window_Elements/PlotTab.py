from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class ConfigurePlotTab(QWidget):

    def __init__(self, plot_tab):
        super(QWidget, self).__init__(plot_tab)

        # add layout to plot
        plot_tab.layout = QGridLayout()
        plot_tab.layout.maximumSize()

        #create 2x2 matrix of layouts to be filled later with plot and settings
        dim_layout = QGridLayout()
        plot_layout = QGridLayout()
        specify_layout = QGridLayout()
        add_layout = QGridLayout()
        
        #configure dim_layout where the user will choose which data/ columns will be plotted
        dim_layout_grid = QGridLayout()
        dim_layout_grid.addWidget(QLabel("DIMENSION"), 0, 0)
        dim_layout_grid.addWidget(QLabel("PLOT TYPE"), 0, 1)
        dim_layout_grid.addWidget(QPushButton("Confirm"), 2, 2)
        x_dim_droplist = QComboBox()
        x_dim_droplist.addItems(["Spalte 1", "Spalte 2", "etc"])
        dim_layout_grid.addWidget(x_dim_droplist, 1, 0)
        dim_layout_grid.addWidget(QLabel("X-DIMENSION"), 1, 1)
        y_dim_droplist = QComboBox()
        y_dim_droplist.addItems(["Spalte 1", "Spalte 2", "etc"])
        dim_layout_grid.addWidget(y_dim_droplist, 2, 0)
        dim_layout_grid.addWidget(QLabel("Y-DIMENSION"), 2, 1)
        z_dim_droplist = QComboBox()
        z_dim_droplist.addItems(["Spalte 1", "Spalte 2", "etc"])
        dim_layout_grid.addWidget(z_dim_droplist, 3, 0)
        dim_layout_grid.addWidget(QLabel("Z-DIMENSION"), 3, 1)
        dim_layout.addLayout(dim_layout_grid, 0, 0)

        #configure layout where plot wil be displayed
        plot_layout_grid = QGridLayout()
        plot_layout_grid.addWidget(QLabel("PLOT"), 0, 0)
        plot_layout.addLayout(plot_layout_grid, 0, 1)

        #specifications of the customize area here
        specify_layout_grid = QGridLayout()
        specify_layout_grid.addWidget(QLabel("SPECIFY"), 0, 0)
        specify_layout.addLayout(specify_layout_grid, 1, 0)

        #buttons to confirm finished plot and add to dashboard
        add_layout_grid = QGridLayout()
        add_layout_grid.addWidget(QLabel("ADD"), 0, 0)
        add_layout.addLayout(add_layout_grid, 1, 1)

        #plot_tab is adding the 4 different layouts
        plot_tab.layout.addLayout(dim_layout, 0, 0)
        plot_tab.layout.addLayout(plot_layout, 0, 1)
        plot_tab.layout.addLayout(specify_layout, 1, 0)
        plot_tab.layout.addLayout(add_layout, 1, 1)
        

        plot_tab.setLayout(plot_tab.layout)