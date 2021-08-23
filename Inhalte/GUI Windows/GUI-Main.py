#Hier kommt der Code für das Hauptfenster rein

import tkinter as tk

window = tk.Tk()
window.title("Graphery")

window.rowconfigure(0, minsize = 800, weight = 1)
window.columnconfigure(1, minsize = 800, weight = 1)

fr_frame = tk.Frame(window)
fr_buttons = tk.Frame(window)
btn_dashboard =tk.Button(fr_buttons, text = "Dashbaord")
btn_Plot =tk.Button(fr_buttons, text = "Plot")
btn_Statistics =tk.Button(fr_buttons, text = "Statistics")
btn_Info =tk.Button(fr_buttons, text = "Info")

btn_dashboard.grid(row=0, column=0, sticky="ew", padx=5, pady=10)
btn_Plot.grid(row=1, column=0, sticky="ew", padx=5, pady=10)
btn_Statistics.grid(row=2, column=0, sticky="ew", padx=5, pady=10)
btn_Info.grid(row=3, column=0, sticky="ew", padx=5, pady=10)

fr_buttons.grid(row=0, column=0, sticky="ns")
fr_frame.grid(row=0, column=1, sticky="nsew")

window.mainloop()