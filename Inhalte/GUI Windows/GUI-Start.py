# open and import window

# imports
from tkinter import Tk, Label, Button

# constants
WINDOW_WIDTH = 900
WINDOW_HEIGHT = 500
DARK_GREEN = "#2F5D62"
GREEN = "#5E8B7E"
LIGHT_GREEN = "#A7C4BC"
LIGHT_LIGHT_GREEN = "#DFEEEA"


# main class: create the start-window
class StartWindow(Tk):
    def __init__(self):
        # initilaize the window
        super().__init__()
        self.title("Import/Open")
        # self.resizable(False, False)
        self.config(padx=50, pady=50, bg=LIGHT_LIGHT_GREEN)
        self.geometry(
            f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}+{int((self.winfo_screenwidth() / 2) - (WINDOW_WIDTH / 2))}+{int((self.winfo_screenheight() / 2) - (WINDOW_HEIGHT / 2))}")

        # Labels
        heading = Label(fg=DARK_GREEN,
                        text="Welcome! This is your personal data visualisation tool.",
                        font=("Helvetica", "23", "bold"),
                        anchor="center",
                        pady=30,
                        bg=LIGHT_LIGHT_GREE
                        )
        heading.grid(column=0, row=0, columnspan=2)

        # Buttons
        btn_open = Button(bg=GREEN, text="Open", fg=DARK_GREEN, width=20, pady=20, padx=20, font=("Arial", "18"))
        btn_import = Button(bg=GREEN, text="Import", fg=DARK_GREEN, width=20, pady=20, padx=20, font=("Arial", "18"))
        btn_import.grid(column=0, row=1)
        btn_open.grid(column=1, row=1)


app = StartWindow()
app.mainloop()
