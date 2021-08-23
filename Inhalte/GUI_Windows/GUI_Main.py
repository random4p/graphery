#Hier kommt der Code für das Hauptfenster rein

import tkinter as tk

class Window():
    
    def __init__(self, master = None):
        self.master = tk.Tk()
        self.master.title("Graphery")

        #set number of rows and columns with size
        #We need 2 only 1 row, but 2 columns -> 1 for the left tab-bar and 1 on the right for the frame in which our target is being visualized
        self.master.rowconfigure(0, minsize = 800, weight = 1)
        self.master.columnconfigure(1, minsize = 800, weight = 1)

        #create Frame for column 1 on the right
        fr_frame = tk.Frame(self.master, bg = "grey")
        #create Frame for column 0 on the left
        fr_buttons = tk.Frame(self.master)

        #initialise all buttons in the tab-box
        btn_dashboard =tk.Button(fr_buttons, text = "Dashbaord")
        btn_Plot =tk.Button(fr_buttons, text = "Plot")
        btn_Statistics =tk.Button(fr_buttons, text = "Statistics")
        btn_Info =tk.Button(fr_buttons, text = "Info")

        #manage position of tab-buttons
        btn_dashboard.grid(row=0, column=0, sticky="ew", padx=5, pady=10)
        btn_Plot.grid(row=1, column=0, sticky="ew", padx=5, pady=10)
        btn_Statistics.grid(row=2, column=0, sticky="ew", padx=5, pady=10)
        btn_Info.grid(row=3, column=0, sticky="ew", padx=5, pady=10)

        #manage position and size of column objects when changing size of window
        fr_buttons.grid(row=0, column=0, sticky="ns")
        fr_frame.grid(row=0, column=1, sticky="nsew")
    def start(self):
        self.master.mainloop()

    

    