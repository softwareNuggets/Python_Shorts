import tkinter as tk
from tkinter import ttk

class BuildListCtrl(tk.Frame):
    def __init__(self, parent, section_title, entry_label_text,
                 background_rgb, foreground_rgb, item_list=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self.background_rgb = background_rgb
        self.foreground_rgb = foreground_rgb
        
        self.section_title = section_title
        self.entry_label_text = entry_label_text
        self.item_list = item_list if item_list is not None else []
        self.selected_index = None
        
        self.create_widgets()

    def create_widgets(self):
        # Frame for entry display
        self.entry_frame = tk.Frame(self, bg=self.background_rgb)
        self.entry_frame.grid(row=0, column=0, columnspan=6, pady=5, sticky='w')

        # Section title
        self.section_title_label = tk.Label(self.entry_frame, 
                                            text=self.section_title, 
                                            font=('Arial', 14, 'bold'),
                                            bg=self.background_rgb, fg=self.foreground_rgb)
        self.section_title_label.grid(row=0, column=0, columnspan=6, pady=5, sticky='w')

        # Entry Label and Entry
        self.entry_label = tk.Label(self.entry_frame, 
                                     text=self.entry_label_text, 
                                     font=('Arial', 12),
                                     bg=self.background_rgb, fg=self.foreground_rgb)
        self.entry_label.grid(row=1, column=0, padx=5, pady=5, sticky='w')

        self.entry_var = tk.StringVar()
        self.entry_box = ttk.Entry(self.entry_frame, textvariable=self.entry_var, width=40)
        self.entry_box.grid(row=1, column=1, padx=(5, 0), pady=5, sticky='w')

        # Buttons
        self.add_button = ttk.Button(self.entry_frame, text="Add", command=self.add_entry)
        self.add_button.grid(row=1, column=2, padx=5, pady=5, sticky='w')

        self.cancel_button = ttk.Button(self.entry_frame, text="Cancel", command=self.cancel_action)
        self.cancel_button.grid(row=1, column=3, padx=5, pady=5, sticky='w')

        self.update_button = ttk.Button(self.entry_frame, text="Update", command=self.update_entry)
        self.update_button.grid(row=1, column=4, padx=5, pady=5, sticky='w')
        self.update_button.grid_remove()

        self.delete_button = ttk.Button(self.entry_frame, text="Delete", command=self.delete_entry)
        self.delete_button.grid(row=1, column=5, padx=5, pady=5, sticky='w')
        self.delete_button.grid_remove()

        # Listbox to display entries
        self.entry_listbox = tk.Listbox(self.entry_frame, height=6, width=50)
        self.entry_listbox.grid(row=2, column=1, columnspan=4, padx=5, pady=5, sticky='w')

        # Bind double click on listbox to load entry name into entry box
        self.entry_listbox.bind('<Double-1>', self.load_entry_to_box)

        # Initial list population
        self.update_entry_listbox()

    def add_entry(self):
        entry_name = self.entry_var.get()
        if not entry_name or entry_name.strip() == "":
            self.entry_box.focus_set()  # Set focus back to the entry box    
            return
        
        self.item_list.append(entry_name)
        self.update_entry_listbox()
        self.clear_entry()
        self.entry_box.focus_set()  # Set focus back to the entry box

    def update_entry(self):
        if self.selected_index is not None:
            self.item_list[self.selected_index] = self.entry_var.get()
            self.update_entry_listbox()
            self.clear_entry()
            self.show_add_cancel_buttons()
            self.entry_box.focus_set()  # Set focus back to the entry box

    def delete_entry(self):
        if self.selected_index is not None:
            del self.item_list[self.selected_index]
            self.update_entry_listbox()
            self.clear_entry()
            self.show_add_cancel_buttons()
            self.entry_box.focus_set()  # Set focus back to the entry box

    def clear_entry(self):
        self.entry_var.set("")

    def cancel_action(self):
        self.clear_entry()
        self.show_add_cancel_buttons()
        self.entry_box.focus_set()  # Set focus back to the entry box

    def load_entry_to_box(self, event):
        self.selected_index = self.entry_listbox.curselection()[0]
        entry_name = self.item_list[self.selected_index]
        self.entry_var.set(entry_name)
        self.show_update_delete_buttons()

    def show_add_cancel_buttons(self):
        self.add_button.grid()
        self.cancel_button.grid()
        self.update_button.grid_remove()
        self.delete_button.grid_remove()

    def show_update_delete_buttons(self):
        self.add_button.grid_remove()
        self.cancel_button.grid()
        self.update_button.grid()
        self.delete_button.grid()

    def update_entry_listbox(self):
        self.entry_listbox.delete(0, tk.END)
        for entry in self.item_list:
            self.entry_listbox.insert(tk.END, entry)
