# open and import window

# imports
from tkinter import Tk, Button, PhotoImage, Canvas, Label, filedialog, Entry
import Data_Manager


# constants
WINDOW_WIDTH = 750
WINDOW_HEIGHT = 400
DARK_GREEN = "#2F5D62"
GREEN = "#5E8B7E"
LIGHT_GREEN = "#A7C4BC"
LIGHT_LIGHT_GREEN = "#DFEEEA"


# --------------------------GET_Name_WINDOW---------------------------------#
class ProjectNameWindow(Tk):
    def close_window(self):
        self.name = self.project_name.get()
        self.destroy()

    def __init__(self):
        super().__init__()
        self.name = "*"
        self.config(padx=50, pady=30, bg=LIGHT_LIGHT_GREEN)
        self.title("Project Name")
        self.geometry(
            f"580x280+{int((self.winfo_screenwidth() / 2) - (WINDOW_WIDTH / 2))}+{int((self.winfo_screenheight() / 2) - (WINDOW_HEIGHT / 2))}")
        label_qst = Label(self, text="How do you want to name your Project?",
                          font=["Helvetica", "18", "bold"], fg=DARK_GREEN)
        label_qst.grid(row=0, column=0, pady=10)
        self.project_name = Entry(self, width=30)
        self.project_name.grid(row=1, column=0, pady=20)
        btn_close = Button(self, text="Okay", command=self.close_window, bg=GREEN, fg="White",
                           width=20, pady=20, padx=20,
                           font=("Arial", "18"), highlightthickness=0,
                           borderwidth=0)
        btn_close.grid(row=2, column=0, pady=10)


# ----------------------------Import_Function----------------------------------#

def import_file():
    # get file from user
    file = filedialog.askopenfile(
        title='Open a file')
    file_type = file.name.split(".")[-1]

    # ask for project name
    name_window = ProjectNameWindow()


    # make our data set structured --> DataManager
    data_set = Data_Manager.DataManager(file, file_type, name_window.name)
    print(data_set.name)

    app.destroy()

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

        self.logo = PhotoImage(file="Images/graphery_logo.png")
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
                            font=("Arial", "18"), highlightthickness=0, borderwidth=0,
                            command=import_file)
        btn_import.grid(column=0, row=1)
        btn_open.grid(column=1, row=1)

        # Labels
        impressum = Label(text="© 2021 eld3niz and random4p", bg=GREEN, fg="White", padx=243)
        impressum.grid(column=0, row=2, columnspan=2, pady=15)


app = StartWindow()
app.mainloop()


