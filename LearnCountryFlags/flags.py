## written by Scott Johnson | @SoftwareNuggets
## Date written: Sep 10, 2024
## Learn country flag
## Youtube :  https://youtube.com/c/softwareNuggets
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import os
import random
import json
import sys
import copy

## install external package
## pip install pillow

# Directory containing flag images
FLAG_DIR = 'country_flags'

regions = ['Africa', 'Asia', 'Caribbean', 'Europe', 'North America', 'Oceania', 'South America']


class QuizApp:
    def __init__(self, root, data=None):
        self.root = root
        self.root.title("Country Flag Quiz by @SoftwareNuggets")
        self.root.geometry("800x700")
        self.root.configure(bg="LightBlue")

        # Make the window non-resizable
        self.root.resizable(False, False)

        self.data = data;
        self.score = 0
        self.total_questions = 0
        self.current_question = 0
        self.num_answers = 4  # Default number of answers
        self.countries_dict = {}
        self.correct_answer = None


        # Initialize the flag label and buttons
        self.flag_label = tk.Label(self.root)
        self.button1 = tk.Button(self.root, text="Button 1", width=40, command=lambda: self.check_answer(0))
        self.button2 = tk.Button(self.root, text="Button 2", width=40, command=lambda: self.check_answer(1))
        self.button3 = tk.Button(self.root, text="Button 3", width=40, command=lambda: self.check_answer(2))
        self.button4 = tk.Button(self.root, text="Button 4", width=40, command=lambda: self.check_answer(3))
        

        # Load country data
        self.file_path = 'AllCountries.json'
        if os.path.exists(self.file_path):
            self.read_json_file(self.file_path)
        else:
            messagebox.showerror("Error", f"File not found: {self.file_path}")
            sys.exit()  # Exit the program if the file doesn't exist

        self.create_widgets()

        # Initialize score label outside of challenge start to avoid overwriting
        self.score_label = tk.Label(self.root, text="Questions: 0 | Correct: 0 | Percentage: 0%")
        self.score_label.grid(row=5, column=0, columnspan=5, pady=10)

        # Hide all buttons initially
        self.hide_buttons()

    def read_json_file(self, file_path):
        """Open and read the JSON file into a dictionary."""
        try:
            with open(file_path, 'r') as file:
                self.data = json.load(file)
        except FileNotFoundError:
            print(f"Error: The file at {file_path} was not found.")
        except json.JSONDecodeError:
            print("Error: The file could not be decoded. Check if it's a valid JSON file.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")     


    def get_countries_by_region(self, region_name, needed):
        
        self.countries_dict = {}
        
        # Check if the region exists in the data
        if region_name in self.data:
            region_data = copy.deepcopy(self.data[region_name])
                        
            for _ in range(len(region_data) + 1):
                if not region_data:
                    break
                count = len(region_data)

                index = random.randint(0, count - 1)
                
                item = region_data[index]
                self.countries_dict[item['country_code']] = item['country_name']
                    
                region_data.pop(index)

                needed = needed - 1
                if needed == 0:
                    break

        else:
            # Return an empty dictionary if the region does not exist
            return {}

    def load_num_of_questions(self, event):
        selected_region = self.region.get()

        region_data = copy.deepcopy(self.data[selected_region])
        max_entries = len(region_data)                
        self.update_option_menu(max_entries)


    def load_countries(self, event):
        num_question = int(self.num_questions_var.get())
        self.get_countries_by_region(selected_region,num_question)

    def hide_buttons(self):
        self.button1.grid_forget()
        self.button2.grid_forget()
        self.button3.grid_forget()
        self.button4.grid_forget()

    def create_widgets(self):
        # Input frame for region, number of answers, and number of questions
        input_frame = ttk.LabelFrame(self.root)
        input_frame.grid(row=0, column=0, rowspan=2, columnspan=5, sticky="nsew", padx=10, pady=10)

        # Configure grid columns for proper alignment
        self.root.grid_columnconfigure(0, weight=1)
        
        self.region = tk.StringVar()
        ttk.Label(input_frame, text="Region").grid(row=0, column=0, padx=15)
        ttk.Label(input_frame, text="Select number of answers:").grid(row=0, column=2, padx=0)
        ttk.Label(input_frame, text="# of Questions:").grid(row=0, column=5, padx=20)

        # Create and place the combo box using grid layout
        self.region_combo = ttk.Combobox(input_frame, textvariable=self.region, state="readonly")
        self.region_combo.grid(row=1, column=0, pady=5, padx=15)
        self.region_combo['values'] = regions
        self.region_combo.bind("<<ComboboxSelected>>", self.load_num_of_questions)
        self.region_combo.set("Select a Region")

        self.num_answers_var = tk.StringVar(value="4")
        self.num_answers_menu = tk.OptionMenu(input_frame, self.num_answers_var, "1", "2", "3", "4")
        self.num_answers_menu.grid(row=1, column=2, pady=5, sticky='s')

        self.num_questions_var = tk.StringVar(value="10")
        self.num_of_questions = tk.OptionMenu(input_frame, self.num_questions_var, "10", "20", "30")
        self.num_of_questions.grid(row=1, column=5, padx=0, sticky='s')

        self.start_button = tk.Button(input_frame, text="Start Quiz", command=self.start_quiz)
        self.start_button.grid(row=2, column=1, pady=10, sticky='w')

        self.reset_button = tk.Button(input_frame, text="Reset", command=self.reset_quiz)
        self.reset_button.grid(row=2, column=2, pady=10, sticky='w')

    def show_buttons(self):
        self.hide_buttons()  # Hide all buttons before showing specific ones

        if self.num_answers == 1:
            self.button1.grid(row=3, column=1, padx=60, pady=5, sticky='we')
        elif self.num_answers == 2:
            self.button1.grid(row=3, column=1, padx=60, pady=5, sticky='we')
            self.button2.grid(row=3, column=2, padx=60, pady=5, sticky='we')
        elif self.num_answers == 3:
            self.button1.grid(row=3, column=1, padx=60, pady=5, sticky='we')
            self.button2.grid(row=3, column=2, padx=60, pady=5, sticky='we')
            self.button3.grid(row=4, column=1, padx=60, pady=5, sticky='we')
        elif self.num_answers == 4:
            self.button1.grid(row=3, column=0, padx=60, pady=5, sticky='we')
            self.button2.grid(row=3, column=1, padx=60, pady=5, sticky='we')
            self.button3.grid(row=4, column=0, padx=60, pady=5, sticky='we')
            self.button4.grid(row=4, column=1, padx=60, pady=5, sticky='we')    

    def start_quiz(self):
        selected_region = self.region_combo.get()

        # Check if a region is selected
        if selected_region == "Select a Region":
            messagebox.showerror("Error", "You must first select a Region")
            return
        
        ## get questionf for selected region, data is already randomized
        num_questions = int(self.num_questions_var.get())
        self.get_countries_by_region(selected_region,num_questions)

        self.current_question = 0
        self.score = 0
        self.num_answers = int(self.num_answers_var.get())
        self.load_images()  # Load flag images
        self.start_new_challenge()
        self.ask_questions(num_questions)

    def load_images(self):
        self.flags = []
        
        # Get list of all filenames in FLAG_DIR
        filenames = [f.lower() for f in os.listdir(FLAG_DIR) if f.endswith(".png")]
        
        # Extract country codes from self.countries_dict
        country_codes = self.countries_dict.keys()
        
        for code in country_codes:
            filename = f"{code.lower()}.png"  # Construct the expected filename
            if filename in filenames:
                try:
                    # Store the code and path to the image
                    self.flags.append((code, os.path.join(FLAG_DIR, filename)))
                except Exception as e:
                    print(f"Error loading image {filename}: {e}")      

        self.total_flags = len(self.flags)
    
    def ask_questions(self, num_questions):
        if self.current_question >= num_questions or self.current_question >= len(self.flags):
            self.show_final_score()
            return

        option_list = []

        ## display question number on screen
        self.current_question += 1
        
        flag_code, flag_path = self.flags[self.current_question-1]
        correct_country = self.countries_dict[flag_code]
        
        country_list = list(self.countries_dict.values())
        country_list.remove(correct_country)
        option_list.append(correct_country)

        for i in range(self.num_answers-1):
            if not country_list:
                break;
            count = len(country_list)
            index = random.randint(0, count - 1)
            option_list.append(country_list[index])
            country_list.remove(country_list[index])
        
        random.shuffle(option_list)
        self.correct_answer = option_list.index(correct_country)  # Set the index of the correct answer


        # Load and display the flag image
        image = Image.open(flag_path)
        image = image.resize((660, 412), Image.LANCZOS)  # Resize image
        self.flag_image = ImageTk.PhotoImage(image)
        self.flag_label.config(image=self.flag_image, width=660, height=412)
        self.flag_label.grid(row=2, column=0, columnspan=5, padx=10, pady=10, sticky='n')
        
        
        self.button1.config(text=option_list[0] if len(option_list) > 0 else "")
        self.button2.config(text=option_list[1] if len(option_list) > 1 else "")
        self.button3.config(text=option_list[2] if len(option_list) > 2 else "")
        self.button4.config(text=option_list[3] if len(option_list) > 3 else "")
        
  
    def update_option_menu(self, max_value):
        # Generate the series based on max_value
        series = self.generate_series(max_value)
        
        # Clear existing options in the OptionMenu
        menu = self.num_of_questions["menu"]
        menu.delete(0, "end")
        
        # Add the new options
        for option in series:
            menu.add_command(label=option, command=tk._setit(self.num_questions_var, option))
        
        # Optionally, you can set the default value to the last item
        self.num_questions_var.set(series[0])


    def generate_series(self, max_value):
        # Handle cases where max_value is less than 10
        if max_value < 10:
            return [str(max_value)]
        
        # Handle cases where max_value is between 10 and 20 (exclusive)
        if max_value < 20:
            return [str(10), str(max_value)]
        
        # Base series for values greater than or equal to 20
        base_series = [10, 20, 30]
        
        if max_value <= base_series[-1]:
            # Create a series with values up to max_value
            series = [x for x in base_series if x <= max_value]
        else:
            # Extend the base series to include max_value
            series = base_series + [max_value]
        
        # Ensure the series contains no more than four elements
        while len(series) > 4:
            series.pop(0)
        
        return [str(num) for num in series]


    def start_new_challenge(self):
            self.show_buttons()
            self.update_score_board()
  
    def check_answer(self, selected_option):
        # First, reset all button colors to the default color
        self.button1.config(bg='SystemButtonFace')
        self.button2.config(bg='SystemButtonFace')
        self.button3.config(bg='SystemButtonFace')
        self.button4.config(bg='SystemButtonFace')

        # Determine which button is the correct one
        
        if 0 <= self.correct_answer < self.num_answers:
            correct_button = [self.button1, self.button2, self.button3, self.button4][self.correct_answer]
        else:
            print(f"Invalid correct_answer index: {self.correct_answer}")
            return

        # Color the correct button green
        correct_button.config(bg='green')

        # Check if the selected button is correct or not
        if selected_option == self.correct_answer:
            self.score += 1
        else:
            # Color the selected wrong answer light pink
            [self.button1, self.button2, self.button3, self.button4][selected_option].config(bg='light pink')

        # Update the score board
        self.update_score_board()
        
        
        # Wait for 1 second and then ask the next question
        self.root.after(1000, self.reset_button_colors)

        # next question
        count = self.num_questions_var.get()
        self.root.after(1000, self.ask_questions, int(count))  

    def reset_button_colors(self):
        # Reset all button colors
        self.button1.config(bg='SystemButtonFace')
        self.button2.config(bg='SystemButtonFace')
        self.button3.config(bg='SystemButtonFace')
        self.button4.config(bg='SystemButtonFace')
    
    def reset_quiz(self):
        self.flag_label.config(image='')
        num_questions_value = int(self.num_questions_var.get())
        self.score = 0
        self.current_question = 0
        self.ask_questions(num_questions_value)  # Restart quiz with 10 questions
        self.update_score_board()


    def show_final_score(self):
        num_questions_value = int(self.num_questions_var.get())
        percentage = (self.score / num_questions_value) * 100
        messagebox.showinfo("Quiz Completed", f"Final Score: {self.score}/{num_questions_value}\nPercentage: {percentage:.2f}%")
        self.score_label.config(text=f"Questions: {num_questions_value} | Correct: {self.score} | Percentage: {percentage:.2f}%")

    def update_score_board(self):
        num_questions_value = int(self.num_questions_var.get())
        num_answers = int(self.num_answers_var.get())

        percentage = (self.score / num_questions_value) * 100  # Assuming 10 questions
        self.score_label.config(text=f"Questions: {num_questions_value} | Correct: {self.score} | Percentage: {percentage:.2f}%")
        
        
if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
