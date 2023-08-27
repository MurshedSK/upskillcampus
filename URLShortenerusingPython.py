# Import necessary libraries
from tkinter import *
import paperclip
import pyperclip
import pyshorteners

# Function to generate and display the shortened URL
def url_shortner():
    # Create an instance of the Shortener class
    shortener = pyshorteners.Shortener()
    
    # Get the URL from the input field and generate the shortened URL
    url_short = shortener.tinyurl.short(main_url.get())
    
    # Set the shortened URL to the StringVar, updating the GUI
    short_url.set(url_short)

# Function to copy the shortened URL to the clipboard
def copy_url():
    # Copy the content of the short_url variable to the clipboard
    pyperclip.copy(short_url.get())

# Main program entry point
if __name__=="__main__":
    # Create the main application window
    root = Tk()
    
    # Set window properties
    root.geometry("800x500")        # Initial window size
    root.maxsize(1920,1080)         # Maximum window size
    root.minsize(650,300)           # Minimum window size
    root.title("My URL Shortener Application")   # Window title
    root.configure(bg="#39f")       # Background color
    
    # Create StringVar variables to store input and output URLs
    main_url = StringVar()          # For the main URL
    short_url = StringVar()         # For the shortened URL
    
    # Create and place GUI elements using Tkinter
    Label(root, text="Enter The Main URL Below", font="poppins", bg = "#936c7d").pack(pady=15)
    Entry(root, textvariable=main_url, width=100).pack(pady=5)
    Button(root, text="Generate Short URL by clicking this link", command=url_shortner).pack(pady=55)
    
    Label(root, text="The Short URL is down below ", font=("poppins", 19, "bold")).pack(pady=7)
    Entry(root, textvariable=short_url, width=50).pack(pady=5)
    Button(root, text="Copy the Short URL", command=copy_url).pack(pady=5)
    
    # Start the GUI event loop to keep the application running
    root.mainloop()
