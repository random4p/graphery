#Hier kommt der Code für das Hauptfenster rein

import tkinter as tk


root = tk.Tk()

canvas = tk.Canvas(root, width=600, height=300)
canvas.grid(columnspan = 3)

#select Image for application
#logo = Image.open()
#logo = ImageTk.PhotoImage(logo)
#logo_label = tk.Label(image=logo)
#logo_label.image = logo
#logo_label.grid(column=1, row = 0)

root.mainloop()