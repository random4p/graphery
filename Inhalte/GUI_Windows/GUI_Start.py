# open and import window

# imports
from tkinter import Tk, Button, PhotoImage, Canvas, Label
import os
from pathlib import Path
# constants
WINDOW_WIDTH = 750
WINDOW_HEIGHT = 400
DARK_GREEN = "#2F5D62"
GREEN = "#5E8B7E"
LIGHT_GREEN = "#A7C4BC"
LIGHT_LIGHT_GREEN = "#DFEEEA"


# main class: create the start-window
class StartWindow(Tk):
    def __init__(self):
        # initialize the window
        super().__init__()
        self.title("Import/Open")
        self.resizable(False, False)
        self.config(padx=50, pady=30, bg=LIGHT_LIGHT_GREEN)
        self.geometry(
            f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}+{int((self.winfo_screenwidth() / 2) - (WINDOW_WIDTH / 2))}+{int((self.winfo_screenheight() / 2) - (WINDOW_HEIGHT / 2))}")

        #searches image path
        #instead of file = file_to_open you can also just do
        # file = graphery_logo.png if that works
        data_folder = Path("Inhalte/GUI_Windows")
        file_to_open = data_folder / "graphery_logo.png"
        self.logo = PhotoImage(file=file_to_open)
        # canvas
        canvas = Canvas(width=650, height=200, bg=DARK_GREEN, borderwidth=0)
        canvas.create_image(150, 100, image=self.logo, state="normal")
        canvas.update()
        canvas.create_text(450, 100, text="Welcome! This is your personal data visualisation tool.",
                           font=["Helvetica", "23", "bold"],
                           fill="White",
                           anchor="center", width=300)
        canvas.grid(column=0, row=0, columnspan=2)

        # Buttons
        btn_open = Button(bg=GREEN, text="Open",
                          fg="White", width=20, pady=20, padx=20,
                          font=("Arial", "18"), highlightthickness=0, borderwidth=0)
        btn_import = Button(bg=GREEN, text="Import",
                            fg="White", width=20, pady=20, padx=20,
                            font=("Arial", "18"), highlightthickness=0, borderwidth=0)
        btn_import.grid(column=0, row=1)
        btn_open.grid(column=1, row=1)

        # Labels
        impressum = Label(text="© 2021 eld3niz and random4p", bg=GREEN, fg="White", padx=243)
        impressum.grid(column=0, row=2, columnspan=2, pady=15)


app = StartWindow()
app.mainloop()
