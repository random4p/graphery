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
        dim_layout_grid.addWidget(confirm_button, 0, 2)
        
        #get all column labels in a list
        drop_list_items = []
        drop_list_items.insert(0, "N/A")

        x_dim_droplist = QComboBox()
        x_dim_droplist.addItems(drop_list_items)
        dim_layout_grid.addWidget(x_dim_droplist, 1, 1)
        dim_layout_grid.addWidget(QLabel("X-DIMENSION"), 1, 0)
        
        y_dim_droplist = QComboBox()
        y_dim_droplist.addItems(drop_list_items)
        dim_layout_grid.addWidget(y_dim_droplist, 2, 1)
        dim_layout_grid.addWidget(QLabel("Y-DIMENSION"), 2, 0)
        
        z_dim_droplist = QComboBox()
        z_dim_droplist.addItems(drop_list_items)
        dim_layout_grid.addWidget(z_dim_droplist, 3, 1)
        dim_layout_grid.addWidget(QLabel("Z-DIMENSION"), 3, 0)
        

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

        plot_label = QLabel("Label of the Plot")
        label_checkbox = QCheckBox()
        dim_layout_grid.addWidget(plot_label, 10, 0)
        dim_layout_grid.addWidget(label_checkbox, 10, 1)
        plot_label_input = QLineEdit()
        plot_label_input.setMaximumWidth(70)
        dim_layout_grid.addWidget(plot_label_input, 10, 2)

        #toggle input box if box is checked or delete if not
        # def add_del_input(box, input, layout):
        #     if box.isChecked() == True:
        #         dim_layout_grid.addWidget(input, 10, 2)
        #     if not box.isChecked() == True:    
        #         #dim_layout_grid.addWidget(QLabel("Mark Box as checked"), 10, 2)
        #         del_input = layout.itemAtPosition(10, 2).widget()
        #         del_input.deleteLater()
            
        # label_checkbox.stateChanged.connect(lambda : add_del_input(label_checkbox, plot_label_input, dim_layout_grid))
        
            
        #configure layout where plot wil be displayed
        plot_layout_grid = QGridLayout()
        test_text = QLabel("PLOT")
        test_text.setMinimumWidth(250)
        plot_layout_grid.addWidget(test_text, 0, 0)
        
        
        #scroll_dim_area.addLayout(dim_layout_grid)
        plot_tab.layout.addWidget(scroll_dim_area, 0, 0)
        plot_tab.layout.addLayout(plot_layout_grid, 0, 1)

        plot_tab.setLayout(plot_tab.layout)