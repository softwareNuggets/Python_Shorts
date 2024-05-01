import sys
import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import requests
from io import BytesIO
from pymongo import MongoClient
from bson import ObjectId
import subprocess

"""
YouTube Channel: https://www.youtube.com/c/softwarenuggets
GitHub           https://github.com/softwareNuggets/Python_Shorts/blob/main/movies_tkInter_mongoDb.py

"""

class MovieApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Movie Search App")

        # MongoDB connection
        self.client = MongoClient('localhost', 27017)
        self.db = self.client['w3c']
        self.movies_collection = self.db['movies']

        self.center_window(self.master)
        self.setup_styles()
        self.create_widgets()
        self.configure_styles()

    def setup_styles(self):
        self.style = ttk.Style()
        self.style.configure('SkyBlue.TLabel', background='sky blue', foreground='black')
        self.style.configure('SkyBlue.TFrame', background='sky blue')

    def center_window(self, window):
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()

        window_width = 900  # Set your desired window width
        window_height = 900  # Set your desired window height

        x = (screen_width // 2) - (window_width // 2)
        y = (screen_height // 2) - (window_height // 2)

        window.geometry(f'{window_width}x{window_height}+{x}+{y}')

    def create_widgets(self):
        # Create a frame to contain the search bar components
        self.search_frame = ttk.Frame(self.master, name="search_frame")
        self.search_frame.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
        self.search_frame.grid_propagate(False)  # Prevent the frame from resizing automatically
        self.search_frame.config(width=850, height=200)      

        # Search bar with label
        self.search_label = ttk.Label(self.search_frame, text="Movie Name:")
        self.search_label.grid(row=0, column=0, padx=10, pady=10)
        self.search_var = tk.StringVar()
        self.search_entry = ttk.Entry(self.search_frame, textvariable=self.search_var)
        self.search_entry.grid(row=0, column=1, padx=10, pady=10)  

        # Actor search
        self.actor_label = ttk.Label(self.search_frame, text="Actor:")
        self.actor_label.grid(row=1, column=0, padx=10, pady=10)
        self.actor_var = tk.StringVar()
        self.actor_entry = ttk.Entry(self.search_frame, textvariable=self.actor_var)
        self.actor_entry.grid(row=1, column=1, padx=10, pady=10)

        # Director search
        self.director_label = ttk.Label(self.search_frame, text="Director:")
        self.director_label.grid(row=2, column=0, padx=10, pady=10)
        self.director_var = tk.StringVar()
        self.director_entry = ttk.Entry(self.search_frame, textvariable=self.director_var)
        self.director_entry.grid(row=2, column=1, padx=10, pady=10)

        # Sort order frame containing radio buttons
        self.sort_order_frame = ttk.Frame(self.search_frame, name="order_by_frame")
        self.sort_order_frame.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky=tk.E)

        self.sort_var = tk.StringVar()
        self.sort_var.set("by movie name")  # Default selection

        self.movie_name_radio = ttk.Radiobutton(self.sort_order_frame, text="By Movie Name", variable=self.sort_var, value="by movie name")
        self.movie_name_radio.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)

        self.year_radio = ttk.Radiobutton(self.sort_order_frame, text="By Year", variable=self.sort_var, value="by year")
        self.year_radio.grid(row=0, column=1, padx=10, pady=5, sticky=tk.W)

        # Buttons row
        self.buttons_frame = ttk.Frame(self.search_frame)
        self.buttons_frame.grid(row=1, column=3, columnspan=2, padx=200, pady=10, sticky=tk.E)

        self.search_button = ttk.Button(self.buttons_frame, text="Search", command=self.search_movies)
        self.search_button.grid(row=0, column=0, padx=10, pady=10)

        self.clear_button = ttk.Button(self.buttons_frame, text="Clear", command=self.clear_search)
        self.clear_button.grid(row=0, column=1, padx=10, pady=10)        

        # Results treeview
        self.tree = ttk.Treeview(self.master, columns=("Title", "IMDb Rating", "Tomatoes Rating", "Directors"), selectmode="browse")
        self.tree.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

        # Set the column headings
        self.tree.heading("#0", text="Year")
        self.tree.heading("Title", text="Title")
        self.tree.heading("IMDb Rating", text="IMDb Rating")
        self.tree.heading("Tomatoes Rating", text="Tomatoes Rating")
        self.tree.heading("Directors", text="Directors")

        # Set the initial width for each column
        self.tree.column("#0", width=80)
        self.tree.column("Title", width=290)
        self.tree.column("IMDb Rating", width=80)
        self.tree.column("Tomatoes Rating", width=105)
        self.tree.column("Directors", width=300)

        # Bind double click event
        self.tree.bind("<Double-1>", self.show_poster)

        # Poster display
        self.plot_frame = ttk.Frame(self.master, name="plot_frame")
        self.plot_frame.grid(row=3, column=0, columnspan=4, padx=10, pady=10, sticky="w")
        self.plot_frame.config(width=850, height=325)
        self.plot_frame.grid_propagate(False)
        self.plot_frame.configure(style='SkyBlue.TFrame')

        self.plot_text = tk.Text(self.plot_frame, wrap="word", height=18, width=82)
        self.plot_text.config(state="disabled")
        self.plot_text.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="w")
        
        self.poster_label = ttk.Label(self.plot_frame, image=None)
        self.poster_label.image = None
        self.poster_label.grid(row=0, column=4, columnspan=4, padx=10, pady=10)


    def configure_styles(self):
        self.search_label.configure(style='SkyBlue.TLabel')
        self.actor_label.configure(style='SkyBlue.TLabel')
        self.director_label.configure(style='SkyBlue.TLabel')
        self.search_frame.configure(style='SkyBlue.TFrame')

    def clear_search(self):
        # Clear the Treeview
        self.tree.delete(*self.tree.get_children())
        self.clear_movie_details()
        self.search_var.set("")
        self.actor_var.set("")
        self.director_var.set("")

    def clear_movie_details(self):
        try:
            if hasattr(self, 'plot_frame') and isinstance(self.plot_frame, (tk.Frame, ttk.Frame)):
                self.plot_text.config(state="normal")
                self.plot_text.delete("1.0", "end")
                self.plot_text.config(state="disabled")
                self.poster_label.configure(image=None)
                self.poster_label.image = None
        except AttributeError:
            pass

    def search_movies(self):
        # Clear the Treeview
        self.tree.delete(*self.tree.get_children())

        # Clear the poster image
        self.poster_label.configure(image=None)

        # Prepare the search queries
        title_query = {"title": {"$regex": self.search_var.get(), "$options": "i"}}
        actor_query = {"cast": {"$regex": self.actor_var.get(), "$options": "i"}}
        director_query = {"directors": {"$regex": self.director_var.get(), "$options": "i"}}

        # Combine all queries with an AND operator
        query = {}
        if self.search_var.get():
            query.update(title_query)
        if self.actor_var.get():
            query.update(actor_query)
        if self.director_var.get():
            query.update(director_query)

        # Perform the search query if at least one condition is specified
        if query:
            # Add sorting based on sort_var
            sort_criteria = [("title", 1)]  # Default sorting by title
            if self.sort_var.get() == "by year":
                sort_criteria = [("year", 1)]

            # Projection to include additional fields
            projection = {"_id": 1, "title": 1, "year": 1, "genres": 1, "poster": 1, "imdb.rating": 1, "tomatoes.viewer.rating": 1, "directors": 1}

            movies = self.movies_collection.find(query, projection).sort(sort_criteria)

            # Populate the Treeview with the search results
            for movie in movies:
                movie_id = movie.get("_id")
                year = movie.get("year", "")
                imdb_rating = movie.get("imdb", {}).get("rating", "")
                tomatoes_rating = movie.get("tomatoes", {}).get("viewer", {}).get("rating", "")
                directors = ", ".join(movie.get("directors", []))

                self.tree.insert("", "end", text=year, values=(movie["title"], imdb_rating, tomatoes_rating, directors, movie_id))

        else:
            # Show a message if no search criteria are provided
            messagebox.showinfo("Info", "Please provide at least one search parameter")


    def show_poster(self, event):
        # Clear previous data
        self.clear_movie_details()

        item = self.tree.selection()[0]
        values = self.tree.item(item, "values")
        movie_id = values[-1]  # Assuming _id or movie_id is the last field in values
        movie = self.movies_collection.find_one({"_id": ObjectId(movie_id)})  # Assuming ObjectId is used for _id
        
        if movie:
            # Display movie plot
            fullplot = movie.get("fullplot", "")
            self.plot_text.config(state="normal")
            self.plot_text.delete("1.0", "end")
            self.plot_text.insert("1.0", fullplot)
            self.plot_text.config(state="disabled")

            # Display movie poster
            if movie.get("poster", ""):
                response = requests.get(movie["poster"])
                if response.status_code == 200:
                    img = Image.open(BytesIO(response.content))
                    img.thumbnail((200, 200))  # Resize image if necessary
                    
                    photo = ImageTk.PhotoImage(img)

                    self.poster_label.configure(image=photo)
                    self.poster_label.image = photo

                    # Open the URL in the default web browser
                    if sys.platform == "win32":   #windows
                        self.poster_label.bind("<Double-1>", lambda event: subprocess.Popen(["start", movie["poster"]], shell=True, start_new_session=True))
                    elif sys.platform == "darwin":  #macOS
                        self.poster_label.bind("<Double-1>", lambda event: subprocess.Popen(["open", movie["poster"]], shell=False, start_new_session=True))
                    else:  #unix-like 
                        self.poster_label.bind("<Double-1>", lambda event: subprocess.Popen(["xdg-open", movie["poster"]], shell=False, start_new_session=True))


                else:
                    messagebox.showerror("Error", "Failed to load poster from URL")
            else:
                messagebox.showinfo("Info", "No poster available for this movie")
        else:
            messagebox.showerror("Error", "Movie not found")

def main():

    root = tk.Tk()
    app = MovieApp(root)
    root.mainloop()

if __name__ == "__main__":
    # Call the main function to start the application
    main()