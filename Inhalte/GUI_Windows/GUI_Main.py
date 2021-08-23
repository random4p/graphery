#Hier kommt der Code für das Hauptfenster rein

import tkinter as tk
from tkinter.ttk import *
from pathlib import Path
from typing import Text

class Window():
    
    def __init__(self, master = None):
        self.master = tk.Tk()
        self.master.minsize(400, 400)
        self.master.title("Graphery")
        tabs = Notebook(self.master)

        tab_dashboard = Frame(self.master)
        tab_plot = Frame(self.master)
        tab_stat = Frame(self.master)
        tab_info = Frame(self.master)

        tabs.add(tab_dashboard, text = "Dashboard")
        tabs.add(tab_plot, text = "Plot")
        tabs.add(tab_stat, text = "Statistics")
        tabs.add(tab_info, text = "Info")
        tabs.pack(expand = True, fill = "both")
        
        Label(tab_dashboard,text="Hello, this is tab#1",width=100).pack()
        Label(tab_plot,text="Hello, this is tab#2",width=100).pack()
        Label(tab_stat,text="Hello, this is tab#3",width=100).pack()
        Label(tab_info,text="Hello, this is tab#4",width=100).pack()

        #function needed for buttons, examples beginning in line 19
    
        def donothing():
             filewin = tk.Toplevel(self.master)
             button = tk.Button(filewin, text="Do nothing button")
             button.pack()
        
        #creates menu bar in top left
        menubar = tk.Menu(self.master)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="New", command=donothing)
        filemenu.add_command(label="Open", command=donothing)
        filemenu.add_command(label="Save", command=donothing)
        filemenu.add_command(label="Save as...", command=donothing)
        filemenu.add_command(label="Close", command=donothing)

        filemenu.add_separator()

        filemenu.add_command(label="Exit", command=self.master.quit)
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

        self.master.config(menu=menubar)

        
        # #set number of rows and columns with size
        # #We need 2 only 1 row, but 2 columns -> 1 for the left tab-bar and 1 on the right for the frame in which our target is being visualized
        # self.master.rowconfigure(0, minsize = 800, weight = 1)
        # self.master.columnconfigure(1, minsize = 800, weight = 1)

        # #create Frame for column 1 on the right
        # fr_frame = tk.Frame(self.master )
        # #create Frame for column 0 on the left
        # fr_buttons = tk.Frame(self.master)

        # #initialise all buttons in the tab-box
        # btn_dashboard =tk.Button(fr_buttons, text = "Dashbaord", height=10, bg = "DeepSkyBlue2", font=("Arial", "12", "bold"))
        # btn_Plot =tk.Button(fr_buttons, text = "Plot", height=10, bg = "DeepSkyBlue2", font=("Arial", "12", "bold"))
        # btn_Statistics =tk.Button(fr_buttons, text = "Statistics", height=10, bg = "DeepSkyBlue2", font=("Arial", "12", "bold"))
        # btn_Info =tk.Button(fr_buttons, text = "Info", height=10, bg = "DeepSkyBlue2", font=("Arial", "12", "bold"))

        # #manage position of tab-buttons
        # btn_dashboard.grid(row=0, column=0, sticky="ew", padx=5, pady=10)
        # btn_Plot.grid(row=1, column=0, sticky="ew", padx=5, pady=10)
        # btn_Statistics.grid(row=2, column=0, sticky="ew", padx=5, pady=10)
        # btn_Info.grid(row=3, column=0, sticky="ew", padx=5, pady=10)

        # #manage position and size of column objects when changing size of window
        # fr_buttons.grid(row=0, column=0, sticky="ns")
        # fr_frame.grid(row=0, column=1, sticky="nsew")


    
    #starts the Application GUI
    def start(self):
        self.master.mainloop()

    

    