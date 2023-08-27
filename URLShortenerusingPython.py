from tkinter import *
import paperclip
import pyperclip
import pyshorteners

def url_shortner():
    shortener = pyshorteners.Shortener()
    url_short = shortener.tinyurl.short(main_url.get())
    
    #set the gloabal short_url
    short_url.set(url_short)

def copy_url():
    #copy short url on clipboard
    pyperclip.copy( short_url.get())

if __name__=="__main__":
    root = Tk()
    root.geometry("800x500")
    root.maxsize(1920,1080)
    root.minsize(650,300)
    root.title("My URL Shortener Application")
    root.configure(bg="#39f")

    main_url = StringVar()
    short_url= StringVar()
    
    Label(root, text="Enter The Main URL Below", font="poppins", bg = "#936c7d").pack(pady=15)
    Entry(root,textvariable=main_url, width =100).pack(pady=5)
    Button(root, text="Generate Short URL by clicking this link", command =url_shortner).pack(pady=55)

    Label(root, text="The Short URL is down below ", font=("poppins", 19, "bold")).pack(pady=7)
    Entry(root, textvariable= short_url, width=50).pack(pady=5)
    Button(root, text="Copy the Short URL", command= copy_url).pack(pady=5)
    root.mainloop()