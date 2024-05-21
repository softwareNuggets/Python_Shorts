import tkinter as tk
from tkinter import ttk
from entry_manager import EntryManager

class MyApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("My Application")
        
        tabControl = ttk.Notebook(self)
        tabControl.pack(expand=1, fill="both")
        
        # Create different instances of EntryManager for different collections
        actors_tab = EntryManager(tabControl, section_title="Actors", entry_label_text="Enter Actor Name")
        directors_tab = EntryManager(tabControl, section_title="Directors", entry_label_text="Enter Director Name")
        teams_tab = EntryManager(tabControl, section_title="Basketball Teams", entry_label_text="Enter Team Name")

        tabControl.add(actors_tab, text="Actors")
        tabControl.add(directors_tab, text="Directors")
        tabControl.add(teams_tab, text="Teams")

if __name__ == "__main__":
    app = MyApp()
    app.mainloop()
