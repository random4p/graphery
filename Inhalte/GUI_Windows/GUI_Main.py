# Hier kommt der Code für das Hauptfenster rein

import tkinter as tk
from tkinter import ttk
from pathlib import Path
from typing import Text
from tkinter.font import BOLD, Font
from ttkthemes import ThemedStyle
import pandas as pd


class Window(tk.Tk):

    def __init__(self, master=None):
        super().__init__()
        self.minsize(1000, 350)
        self.title("Graphery")

        tabs = ttk.Notebook(self)
        style = ThemedStyle(self)
        # style.theme_create("MyStyle", parent="alt", settings={
        # "TNotebook": {"configure": {"tabmargins": [2, 5, 2, 0] } },
        # "TNotebook.Tab": {"configure": {"padding": [90, 20] },}})
        style.theme_use("equilux")

        tab_dashboard = ttk.Frame(self)
        tab_plot = ttk.Frame(self)
        tab_stat = ttk.Frame(self)
        tab_info = ttk.Frame(self)

        tabs.add(tab_dashboard, text="Dashboard")
        tabs.add(tab_plot, text="Plot")
        tabs.add(tab_stat, text="Statistics")
        tabs.add(tab_info, text="Info")
        tabs.pack(expand=True, fill="both")

        # function needed for buttons, examples beginning in line 19
        def donothing():
            filewin = tk.Toplevel(self)
            button = tk.Button(filewin, text="Do nothing button")
            button.pack()

        # creates menu bar in top left
        menubar = tk.Menu(self)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="New", command=donothing)
        filemenu.add_command(label="Open", command=donothing)
        filemenu.add_command(label="Save", command=donothing)
        filemenu.add_command(label="Save as...", command=donothing)
        filemenu.add_command(label="Close", command=donothing)

        filemenu.add_separator()

        filemenu.add_command(label="Exit", command=self.quit)
        menubar.add_cascade(label="File", menu=filemenu)
        editmenu = tk.Menu(menubar, tearoff=0)
        editmenu.add_command(label="Undo", command=donothing)

        editmenu.add_separator()

        editmenu.add_command(label="Cut", command=donothing)
        editmenu.add_command(label="Copy", command=donothing)
        editmenu.add_command(label="Paste", command=donothing)
        editmenu.add_command(label="Delete", command=donothing)
        editmenu.add_command(label="Select All", command=donothing)

        menubar.add_cascade(label="Edit", menu=editmenu)
        helpmenu = tk.Menu(menubar, tearoff=0)
        helpmenu.add_command(label="Info", command=donothing)
        menubar.add_cascade(label="Help", menu=helpmenu)

        self.config(menu=menubar)

        # set number of rows and columns with size
        # We need 2 only 1 row, but 2 columns -> 1 for the left tab-bar and 1 on the right for the frame in which our target is being visualized
        tab_dashboard.rowconfigure(3, minsize=800, weight=1)
        tab_dashboard.columnconfigure(3, minsize=800, weight=1)

        # create Frame for column 1 on the right
        fr_frame = tk.Frame(tab_dashboard)
        # create Frame for column 0 on the left
        fr_buttons = tk.Frame(tab_dashboard)

        # initialise all buttons in the tab-box
        # btn_dashboard =tk.Button(fr_buttons, text = "Object 1", height=10, bg = "DeepSkyBlue2", font=("Arial", "12", "bold"))
        # btn_Plot =tk.Button(fr_buttons, text = "Object 2", height=10, bg = "DeepSkyBlue2", font=("Arial", "12", "bold"))
        # btn_Statistics =tk.Button(fr_buttons, text = "Object 3", height=10, bg = "DeepSkyBlue2", font=("Arial", "12", "bold"))
        # btn_Info =tk.Button(fr_buttons, text = "Object 4", height=10, bg = "DeepSkyBlue2", font=("Arial", "12", "bold"))

        # manage position of tab-buttons
        # btn_dashboard.grid(row=0, column=0, sticky="ew", padx=5, pady=10)
        # btn_Plot.grid(row=1, column=1, sticky="ew", padx=5, pady=10)
        # btn_Statistics.grid(row=2, column=2, sticky="ew", padx=5, pady=10)
        # btn_Info.grid(row=3, column=3, sticky="ew", padx=5, pady=10)

        # manage position and size of column objects when changing size of window
        fr_buttons.grid(row=0, column=0, sticky="ns")
        fr_frame.grid(row=0, column=1, sticky="nsew")

    # starts the Application GUI
    def start(self):
        self.mainloop()
