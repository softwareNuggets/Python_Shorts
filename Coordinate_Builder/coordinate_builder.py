## written by Scott Johnson | @SoftwareNuggets
## Date written: 2/24/2025
## Python: Image Coordinate Builder
## YouTube : https://youtube.com/c/softwareNuggets
## GitHub  : https://github.com/softwareNuggets/Python_Shorts/tree/main/CreateImageMapCoordinates

import tkinter as tk
from tkinter import messagebox, StringVar, filedialog
from PIL import Image, ImageTk, ImageDraw
import os
import sys

class ToolTip:
    """Create a tooltip for a given widget."""
    def __init__(self, widget, text):
        self.widget = widget
        self.text = text
        self.tooltip = None
        self.hide_after_id = None
        
        self.widget.bind("<Enter>", self.show_tooltip)
        self.widget.bind("<Leave>", self.hide_tooltip)

    def show_tooltip(self, event=None):
        """Display the tooltip."""
        if self.tooltip or not event:
            return
        
        x = self.widget.winfo_rootx() + self.widget.winfo_width() // 2
        y = self.widget.winfo_rooty() + self.widget.winfo_height() + 5
        
        # Create tooltip window
        self.tooltip = tk.Toplevel(self.widget)
        self.tooltip.wm_overrideredirect(True)  # Remove window decorations
        self.tooltip.wm_geometry(f"+{x}+{y}")
        
        label = tk.Label(self.tooltip, text=self.text, background="#FFFFDD", 
                          relief="solid", borderwidth=1,padx=5, pady=2)
        label.pack()
        
        # Make sure tooltip is displayed on top
        self.tooltip.lift()

        # Auto-hide after 3 seconds for better UX
        self.widget.after(1500, self.hide_tooltip)

    def hide_tooltip(self, event=None):
        """Hide the tooltip."""
        if self.tooltip:
            self.tooltip.destroy()
            self.tooltip = None
            
class ImageClickApp:
    def __init__(self, window, image_path):
        self.window = window
        self.window.title("Coordinate Builder")
        self.dot_size = 2;
        self.point_color = "blue";
        self.fill_color = "#00990";

        self.window.bind("<Control-z>", lambda e: self.clear_point())
        self.window.bind("<Control-a>", lambda e: self.clear_all_points())
        self.window.bind("<Control-s>", lambda e: self.copy_to_clipboard())
        self.window.bind("<Control-p>", lambda e: self.draw_region())

        # Try to load the image safely
        try:
            self.picture = Image.open(image_path)
            self.picture_tk = ImageTk.PhotoImage(self.picture)
        except FileNotFoundError:
            messagebox.showerror("Error", f"Cannot find image file: {image_path}")
            self.window.destroy()
            return
        except Exception as e:
            messagebox.showerror("Error", f"Cannot load image: {e}")
            self.window.destroy()
            return

        # Create a canvas to display the picture
        self.canvas = tk.Canvas(window, width=self.picture.width, 
                                        height=self.picture.height)
        self.canvas.pack(pady=10)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.picture_tk)

        # List to store clicked points
        self.click_points = []
        
        # Flag to track if a region is drawn
        self.region_drawn = False
        
        # Keep original image for reference
        self.original_image = self.picture.copy()
        self.drawn_image = None

        # Bind the left mouse click event to the canvas
        self.canvas.bind("<Button-1>", self.on_click)

        # Textbox to display points (renamed to segment_boundary)
        self.segment_boundary = tk.Text(window, height=4, width=90)
        self.segment_boundary.pack(pady=10)

        button_frame = tk.Frame(window)
        button_frame.pack(pady=15)

        # Add Clear and Clear All buttons on the same row
        self.clear_button = tk.Button(button_frame, text="Clear",underline=0,
                                      command=self.clear_point)
        self.clear_button.pack(side=tk.LEFT, padx=5)
        
        self.clear_all_button = tk.Button(button_frame, text="Clear All", 
                                    command=self.clear_all_points)
        self.clear_all_button.pack(side=tk.LEFT, padx=5)

        # Add Copy to Clipboard button
        self.copy_button = tk.Button(button_frame, text="Copy to Clipboard", 
                                    command=self.copy_to_clipboard)
        self.copy_button.pack(side=tk.LEFT, padx=5)
        
        # Add Draw button
        self.draw_button = tk.Button(button_frame, text="Paint", 
                                   command=self.draw_region)
        self.draw_button.pack(side=tk.LEFT, padx=5)

        # Add Set Click Points button
        self.assign_click_points_button = tk.Button(button_frame, text="Assign Click Points", 
                                       command=self.assign_click_points)
        self.assign_click_points_button.pack(side=tk.LEFT, padx=5)

        # Add tooltips to buttons
        ToolTip(self.clear_button, "Remove last placed dot <ctrl-z>")
        ToolTip(self.clear_all_button, "Remove all locations dots <ctrl-a>")
        ToolTip(self.copy_button, "Copy the boundary dots INTO the CLIPBOARD <ctrl-s>")
        ToolTip(self.draw_button, "Paint the region enclosed by points <ctrl-p>")
        ToolTip(self.assign_click_points_button,"Assign point to self.click_points object")


        color_frame = tk.Frame(window)
        color_frame.pack(pady=15)

        # Add a label for color selection section
        color_label = tk.Label(color_frame, text="Colors:")
        color_label.pack(side=tk.LEFT, padx=5)

        # Point color selector for dots
        self.point_color_box = tk.Canvas(color_frame, width=20, height=20, bg="blue")
        self.point_color_box.pack(side=tk.LEFT, padx=5)
        point_color_label = tk.Label(color_frame, text="ClickPoint")
        point_color_label.pack(side=tk.LEFT, padx=2)
        self.point_color_box.bind("<Button-1>", self.choose_point_color)

        # Fill color selector for regions
        self.fill_color_box = tk.Canvas(color_frame, width=20, height=20, bg="skyblue")
        self.fill_color_box.pack(side=tk.LEFT, padx=5)
        fill_color_label = tk.Label(color_frame, text="Paint Fill")
        fill_color_label.pack(side=tk.LEFT, padx=2)
        self.fill_color_box.bind("<Button-1>", self.choose_fill_color)

    def choose_point_color(self, event=None):
        """Open a color chooser dialog for point color."""
        from tkinter import colorchooser
        color = colorchooser.askcolor(title="Choose point color")
        if color[1]:  # If a color was selected (not canceled)
            self.point_color_box.config(bg=color[1])
            self.point_color = color[1]


    # And add this method to your ImageClickApp class
    def choose_color(self, event=None):
        """Open a color chooser dialog and set the selected color."""
        from tkinter import colorchooser
        color = colorchooser.askcolor(title="Choose a color")
        if color[1]:  # If a color was selected (not canceled)
            # color[1] is the hex string representation
            self.color_box.config(bg=color[1])
            # Store the selected color for later use (e.g., when drawing regions)
            self.current_color = color[1]

            if hasattr(self, 'current_color_tooltip'):
                self.current_color_tooltip.text = f"Boundary color: {color[1]}"
            else:
                self.current_color_tooltip = ToolTip(self.color_box, f"Boundary color: {color[1]}")
           
    def choose_fill_color(self, event=None):
        """Open a color chooser dialog and set the selected fill color."""
        from tkinter import colorchooser
        color = colorchooser.askcolor(title="Choose fill color")
        if color[1]:  # If a color was selected (not canceled)
            # color[1] is the hex string representation
            self.fill_color_box.config(bg=color[1])
            # Store the selected fill color for region drawing
            self.fill_color = color[1]
            
            if hasattr(self, 'fill_color_tooltip'):
                self.fill_color_tooltip.text = f"Fill color: {color[1]}"
            else:
                self.fill_color_tooltip = ToolTip(self.fill_color_box, f"Fill color: {color[1]}")


    def update_textbox(self):
        """Update the segment_boundary with the formatted click points."""
        formatted_text = '"location_name": ['
        formatted_text += ", ".join([f"({x},{y})" for (x, y) in self.click_points])
        formatted_text += "]"

        self.segment_boundary.delete("1.0", tk.END)  # Clear previous text
        self.segment_boundary.insert(tk.END, formatted_text)  # Insert updated text

    def clear_all_points(self):
        """Remove all clicked points and drawn regions."""
        self.click_points.clear()
        self.region_drawn = False
        # Reset to original image
        self.picture = self.original_image.copy()
        self.picture_tk = ImageTk.PhotoImage(self.picture)
        self.show_points()              # Update the display
        self.update_textbox()           # Clear the segment_boundary
        
    def clear_point(self):
        """Remove the most recent clicked point."""
        if self.click_points:           # Check if the list is not empty
            self.click_points.pop()     # Remove the last element
            
            # If region was drawn, redraw without it
            if self.region_drawn:
                self.picture = self.original_image.copy()
                self.picture_tk = ImageTk.PhotoImage(self.picture)
                self.region_drawn = False
                
            self.show_points()          # Update the display
            self.update_textbox()       # Update the segment_boundary
        else:
            print("No points to remove!")  # Optional feedback

    def show_points(self):
        """Draw all clicked points on the image."""
        self.canvas.delete("all")  # Clear previous drawings
        self.canvas.create_image(0, 0, anchor="nw", image=self.picture_tk)
        for x, y in self.click_points:
            # Draw dots using the selected point color
            self.canvas.create_oval(x-self.dot_size, y-self.dot_size, 
                    x+self.dot_size, y+self.dot_size, fill=self.point_color)

    def draw_region(self):
        """Draw the region enclosed by the points."""
        if len(self.click_points) < 3:
            messagebox.showwarning("Not Enough Points", "Need at least 3 points to draw a region!")
            return
            
        # Create a copy of the original image to draw on
        self.picture = self.original_image.copy()
        draw = ImageDraw.Draw(self.picture, 'RGBA')
        
        # Convert hex color to RGBA tuple with transparency
        if len(self.fill_color)==7 and self.fill_color[0]=='#':
            fill_color = self.fill_color
            r = int(fill_color[1:3], 16)
            g = int(fill_color[3:5], 16)
            b = int(fill_color[5:7], 16)
        else:
            messagebox.showwarning("Select Paint fill", "Reselect a Paint Fill Color!")
            return
        
        # Draw polygon with selected color (with transparency)
        draw.polygon(self.click_points, fill=(r, g, b, 128))
        
        # Update the display image
        self.picture_tk = ImageTk.PhotoImage(self.picture)
        self.region_drawn = True
        self.show_points()  # This will redraw the image and points
        
        # Save the drawn image for reference
        self.drawn_image = self.picture.copy()

    def copy_to_clipboard(self):
        """Copy the content of segment_boundary to clipboard with color feedback."""
        if not self.click_points:
            messagebox.showwarning("No Data", "No points to copy!")
            return
            
        # Get the text from segment_boundary
        content = self.segment_boundary.get("1.0", tk.END).strip()
        
        # Clear clipboard and append new content
        self.window.clipboard_clear()
        self.window.clipboard_append(content)
        
        # Visual feedback - change background color temporarily
        original_bg = self.segment_boundary.cget("background")  # Store original background color
        self.segment_boundary.config(background="light sky blue")

        # Schedule color change back after 1 second
        self.window.after(1000, lambda: self.segment_boundary.config(background=original_bg))

    def assign_click_points(self):
        # Get the text from the Text widget
        input_string = self.segment_boundary.get("1.0", tk.END).strip()
        if not input_string:
            messagebox.showwarning("Warning", "No coordinates to set!")
            return


        # Remove newline, tab, and space characters
        input_string = input_string.replace('\n', '').replace('\t', '').replace(' ', '')

        try:
            # Ensure the input contains the expected format
            if '[(' not in input_string or ')]' not in input_string:
                raise ValueError("Invalid format: Missing expected '[(' or ')]'")

            # Extract the points substring
            points_str = input_string.split('[(')[1].split(')]')[0]

            # Validate that the extracted string matches the expected format
            if not points_str:
                raise ValueError("Invalid format: No coordinate data found")

            # Split the string into individual coordinate pairs
            point_pairs = points_str.split('),(')

            # Convert each pair to a tuple of integers
            self.click_points = []
            for pair in point_pairs:
                # Remove any remaining parentheses and split by comma
                x, y = pair.replace('(', '').replace(')', '').split(',')

                # Convert to integers and store in list
                self.click_points.append((int(x), int(y)))

                print(f"Set Name: {self.click_points}")

        except ValueError as ve:
            print(f"ValueError: {ve}")
            messagebox.showerror("Error", str(ve))
        except Exception as e:
            print(f"Error parsing input: {e}")
            messagebox.showerror("Error", "Invalid format for coordinates. Please check and try again.")


    def on_click(self, event):
        """Handle mouse click events on the image."""
        x, y = event.x, event.y
        self.click_points.append((x, y))
        print(f"Clicked at: ({x}, {y})")
        
        # If region was drawn, clear it
        if self.region_drawn:
            self.picture = self.original_image.copy()
            self.picture_tk = ImageTk.PhotoImage(self.picture)
            self.region_drawn = False
            
        self.show_points()
        self.update_textbox()           # Update textbox with new points
   
        
# Run the application
if __name__ == "__main__":
    # Create the main window first
    window = tk.Tk()
    
    window.withdraw()  # Hide the main window temporarily

    # Open file picker dialog
    image_path = filedialog.askopenfilename(
        title="Select Image File",
        filetypes=[
            ("PNG files", "*.png"),
            ("JPEG files", "*.jpg *.jpeg"),
            ("GIF files", "*.gif"),
            ("BMP files", "*.bmp"),
            ("All files", "*.*")
        ]
    )

    # Check if a file was selected
    if not image_path:
        messagebox.showerror("Error", "No image file selected!")
        window.quit()
        exit()

    # Check if the selected file exists
    if not os.path.exists(image_path):
        messagebox.showerror("Error", f"File '{image_path}' does not exist!")
        window.quit()
        exit()

    # Recreate the window and show the app
    window.deiconify()  # Show the window
    window.geometry("1284x928")
    app = ImageClickApp(window, image_path)
    window.mainloop()
