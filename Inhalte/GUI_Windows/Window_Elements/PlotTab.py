from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import pandas as pd
import random
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
from Data_Manager import DataManager

class ConfigurePlotTab(QWidget):

    def __init__(self, plot_tab, data_set, parent):
    #def __init__(self, plot_tab):
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

        # configure area where settings will be done
        dim_layout_grid.setVerticalSpacing(60)
        dim_layout_grid.setContentsMargins(-2, 0, 0, 0)
        dim_label = QLabel("DIMENSION")
        dim_label.setMaximumHeight(25)
        plot_label= QLabel("PLOT")
        plot_label.setMaximumHeight(25)
        dim_layout_grid.addWidget(dim_label, 0, 0)
        dim_layout_grid.addWidget(plot_label, 0, 1)
        
        #confirm button to start plotting
        confirm_button = QPushButton("Confirm")
        confirm_button.setMaximumWidth(40)
        dim_layout_grid.addWidget(confirm_button, 0, 2)
        
        #get all column labels in a list
        self.data = data_set
        self.drop_list_items = self.data.get_DataFrame_cl()
        self.drop_list_items.insert(0, "N/A")
        
        #choose column to get data from 
        self.x_dim_droplist = QComboBox()
        self.x_dim_droplist.addItems(self.drop_list_items)
        dim_layout_grid.addWidget(self.x_dim_droplist, 1, 1)
        dim_layout_grid.addWidget(QLabel("X-DIMENSION"), 1, 0)
        
        #choose column to get data from
        self.y_dim_droplist = QComboBox()
        self.y_dim_droplist.addItems(self.drop_list_items)
        dim_layout_grid.addWidget(self.y_dim_droplist, 2, 1)
        dim_layout_grid.addWidget(QLabel("Y-DIMENSION"), 2, 0)
        
        #choose column to get data from
        self.z_dim_droplist = QComboBox()
        self.z_dim_droplist.addItems(self.drop_list_items)
        dim_layout_grid.addWidget(self.z_dim_droplist, 3, 1)
        dim_layout_grid.addWidget(QLabel("Z-DIMENSION"), 3, 0)

        #selection box to determine which plot will be used
        select_plot = QLabel("Select Plot")
        select_plot.setMaximumWidth(70)
        self.select_plot_value = QComboBox()
        self.list_of_plots = [
                                "Plot-Type",
                                "Line Plot", 
                                "Bar Graph", 
                                "Histogram", 
                                "Scatter", 
                                "Area Plot", 
                                "Pie Chart", 
                                "Box Plot", 
                                "Hexagonal bin Plot", 
                                "Density Plot", 
                                "Andrews curves", 
                                "Parallel Coordinates", 
                                "Lag plot", 
                                "Autocorrelation plot", 
                                "Bootstrap plot", 
                                "RadViz"
                            ]
        self.select_plot_value.addItems(self.list_of_plots)
        dim_layout_grid.addWidget(select_plot, 1, 2)
        dim_layout_grid.addWidget(self.select_plot_value, 2, 2)


        #set some filters for plot
        dim_layout_grid.addWidget(QLabel("FILTER X-DIM"), 4, 0)
        x_filter_droplist = QComboBox()
        x_filter_droplist.addItems(["N/A", "=","<", ">", ">=", "<="])
        dim_layout_grid.addWidget(x_filter_droplist, 4, 1)
        xfilter_input = QLineEdit()
        xfilter_input.setMaximumWidth(70)
        dim_layout_grid.addWidget(xfilter_input, 4, 2)

        dim_layout_grid.addWidget(QLabel("FILTER #2 X-DIM"), 5, 0)
        x_filter2_droplist = QComboBox()
        x_filter2_droplist.addItems(["N/A", "=","<", ">", ">=", "<="])
        dim_layout_grid.addWidget(x_filter2_droplist, 5, 1)
        xfilter2_input = QLineEdit()
        xfilter2_input.setMaximumWidth(70)
        dim_layout_grid.addWidget(xfilter2_input, 5, 2)

        dim_layout_grid.addWidget(QLabel("FILTER Y-DIM"), 6, 0)
        y_filter_droplist = QComboBox()
        y_filter_droplist.addItems(["N/A", "=","<", ">", ">=", "<="])
        dim_layout_grid.addWidget(y_filter_droplist, 6, 1)
        yfilter_input = QLineEdit()
        yfilter_input.setMaximumWidth(70)
        dim_layout_grid.addWidget(yfilter_input, 6, 2)

        dim_layout_grid.addWidget(QLabel("FILTER #2 Y-DIM"), 7, 0)
        y_filter2_droplist = QComboBox()
        y_filter2_droplist.addItems(["N/A", "=","<", ">", ">=", "<="])
        dim_layout_grid.addWidget(y_filter2_droplist, 7, 1)
        yfilter2_input = QLineEdit()
        yfilter2_input.setMaximumWidth(70)
        dim_layout_grid.addWidget(yfilter2_input, 7, 2)

        dim_layout_grid.addWidget(QLabel("FILTER Z-DIM"), 8, 0)
        z_filter_droplist = QComboBox()
        z_filter_droplist.addItems(["N/A", "=","<", ">", ">=", "<="])
        dim_layout_grid.addWidget(z_filter_droplist, 8, 1)
        zfilter_input = QLineEdit()
        zfilter_input.setMaximumWidth(70)
        dim_layout_grid.addWidget(zfilter_input, 8, 2)

        dim_layout_grid.addWidget(QLabel("FILTER #2 Z-DIM"), 9, 0)
        z_filter2_droplist = QComboBox()
        z_filter2_droplist.addItems(["N/A", "=","<", ">", ">=", "<="])
        dim_layout_grid.addWidget(z_filter2_droplist, 9, 1)
        zfilter2_input = QLineEdit()
        zfilter2_input.setMaximumWidth(70)
        dim_layout_grid.addWidget(zfilter2_input, 9, 2)
 
 
        ######plot layout
        plot_layout_grid = QGridLayout()
        plot_layout_inside_grid = QVBoxLayout()

        plot_layout_inside_grid.figure = plt.figure()
        plot_layout_inside_grid.canvas = FigureCanvas(plot_layout_inside_grid.figure)
        plot_layout_inside_grid.toolbar = NavigationToolbar(plot_layout_inside_grid.canvas, parent)
        

        add_dashboard_button = QPushButton('Add Dashboard')
        #add_dashboard_button.clicked.connect(add_dash)
        
        def plot_now():
        
            # random data
            data = [random.random() for i in range(10)]
            test_list = ["N{ini}".format(ini = i) for i in range(10)]

            #values of colums

            # instead of ax.hold(False)
            plot_layout_inside_grid.figure.clear()

            # create an axis
            ax = plot_layout_inside_grid.figure.add_subplot(111)

            # discards the old graph
            if self.select_plot_value.currentText() == "Line Plot":
                ax.plot(test_list,data)

            if self.select_plot_value.currentText() == "Scatter":
                ax.scatter(test_list,data)

            if self.select_plot_value.currentText() == "Pie Chart":
                ax.pie(data, autopct='%1.1f%%', labels = data, startangle=90)
                ax.axis('equal')

            # refresh canvas
            plot_layout_inside_grid.canvas.draw()
        
        confirm_button.clicked.connect(plot_now)
        plot_layout_inside_grid.addWidget(plot_layout_inside_grid.toolbar)
        plot_layout_inside_grid.addWidget(plot_layout_inside_grid.canvas)
        plot_layout_inside_grid.addWidget(add_dashboard_button)
        plot_layout_grid.addLayout(plot_layout_inside_grid, 0, 0)
        
        
        plot_tab.layout.addWidget(scroll_dim_area, 0, 0)
        plot_tab.layout.addLayout(plot_layout_grid, 0, 1)

        plot_tab.setLayout(plot_tab.layout)