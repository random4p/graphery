from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class ConfigurePlotTab(QWidget):

    def __init__(self, plot_tab):
        super(QWidget, self).__init__(plot_tab)

        # add layout to plot
        plot_tab.layout = QGridLayout()
        plot_tab.layout.maximumSize()

        #create 1x2 matrix of layouts to be filled later with plot and settings
        #configure dim_layout where the user will choose which data/ columns will be plotted
        scroll_dim_area = QScrollArea()
        scroll_dim_area.setMaximumWidth(300)
        scroll_dim_area.setWidgetResizable(True)
        scrollAreaWidgetContents = QWidget()
        dim_layout_grid = QGridLayout(scrollAreaWidgetContents)
        scroll_dim_area.setWidget(scrollAreaWidgetContents)

        
        dim_layout_grid.setVerticalSpacing(60)
        dim_layout_grid.setContentsMargins(-2, 0, 0, 0)
        dim_label = QLabel("DIMENSION")
        dim_label.setMaximumHeight(25)
        plot_label= QLabel("PLOT")
        plot_label.setMaximumHeight(25)
        dim_layout_grid.addWidget(dim_label, 0, 0)
        dim_layout_grid.addWidget(plot_label, 0, 1)
        
        confirm_button = QPushButton("Confirm")
        confirm_button.setMaximumWidth(40)
        dim_layout_grid.addWidget(confirm_button, 2, 2)
        
        x_dim_droplist = QComboBox()
        x_dim_droplist.addItems(["None", "Spalte 1", "Spalte 2", "etc"])
        dim_layout_grid.addWidget(x_dim_droplist, 1, 0)
        dim_layout_grid.addWidget(QLabel("X-DIMENSION"), 1, 1)
        
        y_dim_droplist = QComboBox()
        y_dim_droplist.addItems(["None","Spalte 1", "Spalte 2", "etc"])
        dim_layout_grid.addWidget(y_dim_droplist, 2, 0)
        dim_layout_grid.addWidget(QLabel("Y-DIMENSION"), 2, 1)
        
        z_dim_droplist = QComboBox()
        z_dim_droplist.addItems(["None","Spalte 1", "Spalte 2", "etc"])
        dim_layout_grid.addWidget(z_dim_droplist, 3, 0)
        dim_layout_grid.addWidget(QLabel("Z-DIMENSION"), 3, 1)
        

        dim_layout_grid.addWidget(QLabel("FILTER X-DIM"), 4, 0)
        x_filter_droplist = QComboBox()
        x_filter_droplist.addItems(["None","Spalte 1", "Spalte 2", "etc"])
        dim_layout_grid.addWidget(x_filter_droplist, 4, 1)
        xfilter_input = QLineEdit()
        xfilter_input.setMaximumWidth(70)
        dim_layout_grid.addWidget(xfilter_input, 4, 2)

        dim_layout_grid.addWidget(QLabel("FILTER #2 X-DIM"), 5, 0)
        x_filter2_droplist = QComboBox()
        x_filter2_droplist.addItems(["None","Spalte 1", "Spalte 2", "etc"])
        dim_layout_grid.addWidget(x_filter2_droplist, 5, 1)

        dim_layout_grid.addWidget(QLabel("FILTER Y-DIM"), 6, 0)
        y_filter_droplist = QComboBox()
        y_filter_droplist.addItems(["None","Spalte 1", "Spalte 2", "etc"])
        dim_layout_grid.addWidget(y_filter_droplist, 6, 1)

        dim_layout_grid.addWidget(QLabel("FILTER #2 Y-DIM"), 7, 0)
        y_filter2_droplist = QComboBox()
        y_filter2_droplist.addItems(["None","Spalte 1", "Spalte 2", "etc"])
        dim_layout_grid.addWidget(y_filter2_droplist, 7, 1)

        dim_layout_grid.addWidget(QLabel("FILTER Z-DIM"), 8, 0)
        z_filter_droplist = QComboBox()
        z_filter_droplist.addItems(["None","Spalte 1", "Spalte 2", "etc"])
        dim_layout_grid.addWidget(z_filter_droplist, 8, 1)

        dim_layout_grid.addWidget(QLabel("FILTER Z-DIM"), 9, 0)
        z_filter2_droplist = QComboBox()
        z_filter2_droplist.addItems(["None","Spalte 1", "Spalte 2", "etc"])
        dim_layout_grid.addWidget(z_filter2_droplist, 9, 1)

        #configure layout where plot wil be displayed
        plot_layout_grid = QGridLayout()
        test_text = QLabel("PLOT")
        test_text.setMinimumWidth(250)
        plot_layout_grid.addWidget(test_text, 0, 0)
        
        
        #scroll_dim_area.addLayout(dim_layout_grid)
        plot_tab.layout.addWidget(scroll_dim_area, 0, 0)
        plot_tab.layout.addLayout(plot_layout_grid, 0, 1)

        plot_tab.setLayout(plot_tab.layout)