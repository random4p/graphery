import sys

from PyQt5.QtWidgets import (
    QApplication,
    QCheckBox,
    QTabWidget,
    QVBoxLayout,
    QWidget,
)

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Graphery")
        self.resize(600, 400)
        # Create a top-level layout
        layout = QVBoxLayout()
        self.setLayout(layout)
        # Create the tab widget with two tabs
        tabs = QTabWidget()
        tabs.addTab(self.dashboard_grid(), "Dashboard")
        tabs.addTab(self.plot_Tab_UI(), "Plot")
        tabs.addTab(self.stat_Tab_UI(), "Statistics")
        tabs.addTab(self.info_Tab_UI(), "Info")
        layout.addWidget(tabs)

    def dashboard_grid(self):
        """Create the dashboard page UI."""
        dashboardTab = QWidget()
        dashboardTab.setStyleSheet("QTabBar::tab { height: 100px; width: 100px; background: 'red'}")
        layout = QVBoxLayout()
        layout.addWidget(QCheckBox("General Option 1"))
        layout.addWidget(QCheckBox("General Option 2"))
        dashboardTab.setLayout(layout)
        return dashboardTab

    def plot_Tab_UI(self):
        """Create the plot page UI."""
        plotTab = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(QCheckBox("Network Option 1"))
        layout.addWidget(QCheckBox("Network Option 2"))
        plotTab.setLayout(layout)
        return plotTab

    def stat_Tab_UI(self):
        """Create the stat page UI."""
        statTab = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(QCheckBox("Network Option 1"))
        layout.addWidget(QCheckBox("Network Option 2"))
        statTab.setLayout(layout)
        return statTab

    def info_Tab_UI(self):
        """Create the info page UI."""
        infoTab = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(QCheckBox("Network Option 1"))
        layout.addWidget(QCheckBox("Network Option 2"))
        infoTab.setLayout(layout)
        return infoTab

