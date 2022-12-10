# Import the necessary modules
import tkinter as tk
from tkinter import ttk
from tkinter import font
from PIL import ImageTk, Image
import requests
from io import BytesIO

# Set the URL for the image API
URL = "https://source.unsplash.com/random"

# Define the GUI
class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)

        # Create a font for the title label
        title_font = font.Font(family="Helvetica", size=18, weight="bold")

        # Create a title label
        self.title_label = ttk.Label(self, text="Random Image", font=title_font)
        self.title_label.pack(side="top")

        # Create a frame to hold the image
        self.image_frame = ttk.Frame(self)
        self.image_frame.pack(side="top")

        # Set the initial image
        self.set_image()

        # Create a button to refresh the image
        self.refresh_button = ttk.Button(self, text="Refresh", command=self.set_image)
        self.refresh_button.pack(side="bottom")

    def set_image(self):
        # Download a random image from the URL
        response = requests.get(URL)
        img = Image.open(BytesIO(response.content))

        # Resize the image
        img = img.resize((400, 400), Image.ANTIALIAS)

        # Create a PhotoImage object to display the image
        self.photo = ImageTk.PhotoImage(img)

        # Create a label to display the image
        self.image_label = ttk.Label(self.image_frame, image=self.photo)
        self.image_label.pack()

# Run the application
if __name__ == "__main__":
    app = App()
    app.mainloop()

    
    
    
    
    
    
    
    OR
    
    
    
    
    
    
    
    
    
    
    
    
    
    
import tkinter as tk
from PIL import Image, ImageTk
import requests
from io import BytesIO

# Create a new Tkinter window
window = tk.Tk()

# Create a function to be called when the button is clicked
def show_random_image():
    # Use the requests library to download a random image from the internet
    image_data = requests.get('https://source.unsplash.com/random').content
    
    # Use the BytesIO class to create a file-like object from the image data
    image_file = BytesIO(image_data)
    
    # Use the Image class from the PIL library to open the image file
    image = Image.open(image_file)
    
    # Use the ImageTk class to convert the image to a Tkinter-compatible photo image
    photo = ImageTk.PhotoImage(image)
    
    # Display the image in the window
    window.image_label.config(image=photo)
    window.image_label.image = photo

# Create a button to trigger the image display
button = tk.Button(window, text="Show Image", command=show_random_image)
button.pack()

# Create a label to display the image
image_label = tk.Label(window)
image_label.pack()

# Start the Tkinter event loop
window.mainloop()
