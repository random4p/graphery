# open and import window

# imports
import sys
#from Inhalte.GUI_Windows.GUI_Main import Window
#from Inhalte.GUI_Windows import Data_Manager
from GUI_Main import Window
import Data_Manager
from PyQt5.QtWidgets import QApplication
from tkinter import Tk, Button, PhotoImage, Canvas, Label, filedialog, Entry, messagebox
from os import listdir
from os.path import isfile, join

# constants
WINDOW_WIDTH = 750
WINDOW_HEIGHT = 420
DARK_GREEN = "#2F5D62"
GREEN = "#5E8B7E"
LIGHT_GREEN = "#A7C4BC"
LIGHT_LIGHT_GREEN = "#DFEEEA"

existing_projects = [f.split(".")[0] for f in listdir("Database") if isfile(join("Database", f))]
#existing_projects = [f.split(".")[0] for f in listdir("Inhalte/GUI_Windows/Database") if isfile(join("Inhalte/GUI_Windows/Database", f))]

# ----------------------------Import_Function----------------------------------#
# missing that the user can only open or import a file if he has entered a name in the entry field !!!

def import_file():
    # get file from user
    try:
        file = filedialog.askopenfile(
            title='Open a file')
        file_type = file.name.split(".")[-1]
        name = app.entry_name.get()
        data_set = Data_Manager.DataManager(file, file_type, name)
        app.destroy()
        print("DATA LOADED")

        if __name__ == '__main__':
            print("START MAIN")
            main = QApplication(sys.argv)
            main.setStyle("Fusion")
            ex = Window(data_set)
            print("END MAIN")
            sys.exit(main.exec_())
    except FileNotFoundError:
        print("File was not found.")
    except AttributeError:
        print("Object does not have this attribute.")

def open_file():
    if app.entry_name.get() in existing_projects:
        data_set = Data_Manager.DataManager(name=app.entry_name.get(), mode="open")
        app.destroy()
        if __name__ == '__main__':
            main = QApplication(sys.argv)
            main.setStyle("Fusion")
            ex = Window(data_set)
            sys.exit(main.exec_())
    else:
        messagebox.showerror("FileNotFoundError", "This file does not exist. Maybe you want to import a data set.")


# ----------------------------Start_WINDOW-----------------------------------#
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

        # canvas
        self.logo = PhotoImage(file="Images/graphery_logo.png")
        #self.logo = PhotoImage(file="Inhalte/GUI_Windows/Images/graphery_logo.png")
        canvas = Canvas(width=650, height=200, bg=DARK_GREEN, borderwidth=0)
        canvas.create_image(150, 100, image=self.logo, state="normal")
        canvas.update()
        canvas.create_text(450, 100, text="Welcome! This is your personal data visualisation tool.",
                           font=["Helvetica", "23", "bold"],
                           fill="White",
                           anchor="center", width=300)
        canvas.grid(column=0, row=0, columnspan=2)

        # Entry
        self.entry_name = Entry(width=40)
        self.entry_name.grid(column=1, row=1, pady=10, padx=10)

        # Buttons
        self.btn_open = Button(bg=GREEN, text="Open",
                          fg="White", width=20, pady=20, padx=20,
                          font=("Arial", "18"), highlightthickness=0, borderwidth=0,
                          command=open_file, state="disabled")
        self.btn_import = Button(bg=GREEN, text="Import",
                            fg="White", width=20, pady=20, padx=20,
                            font=("Arial", "18"), highlightthickness=0, borderwidth=0,
                            command=import_file, state="disabled")
        self.btn_import.grid(column=0, row=2)
        self.btn_open.grid(column=1, row=2)

        # Labels
        project_name_label = Label(text="Enter the project name:", font=("Arial", 15, "bold"))
        project_name_label.grid(row=1, column=0, pady=10, sticky="e")
        creator_label = Label(text="© 2021 eld3niz and random4p", bg=GREEN, fg="White", padx=243)
        creator_label.grid(column=0, row=3, columnspan=2, pady=15)

    # functionality -- enable und disable button
    def check_window(self, function):
        self.after(100, func=function)

    def check_entry_field(self):
        if self.entry_name.get() != "":
            self.btn_import.config(state="normal")
            self.btn_open.config(state="normal")
            self.check_window(self.check_entry_field)
        else:
            self.btn_import.config(state="disabled")
            self.btn_open.config(state="disabled")
            self.check_window(self.check_entry_field)

app = StartWindow()
app.check_window(app.check_entry_field)
app.mainloop()
