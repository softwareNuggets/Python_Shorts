import tkinter as tk
from tkinter import ttk
from build_list_ctrl import BuildListCtrl

class MyApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Youtube - Build List Ctrl")

        tabControl = ttk.Notebook(self)
        tabControl.pack(expand=1, fill="both")

        states_tab = BuildListCtrl(tabControl,
                                   section_title="USA States",
                                   entry_label_text="Enter State Name",
                                   background_rgb="#c1d7e6",
                                   foreground_rgb="#000000")
        tabControl.add(states_tab, text="USA States")

        teams_tab = BuildListCtrl(tabControl,
                                  section_title="Basketball Teams",
                                  entry_label_text="Enter Team Name",
                                  background_rgb="#ffe19c",
                                  foreground_rgb="#000000")
        tabControl.add(teams_tab, text="NBA Teams")

        actors_tab = BuildListCtrl(tabControl,
                                   section_title="Movie Actors",
                                   entry_label_text="Enter Actor Name",
                                   background_rgb="#e3c1e6",
                                   foreground_rgb="#000000")
        tabControl.add(actors_tab, text="Movie Actors")

if __name__ == "__main__":
    app = MyApp()
    app.mainloop()
