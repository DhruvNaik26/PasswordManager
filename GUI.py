# This code is fr experiment purpose where we will be testing different gui's is python for the project
from tkinter import *  # type: ignore # Import everything from tkinter 
import customtkinter as ck # Import customtkinter for enhanced tkinter widgets


# Set the appearance mode and default color theme
ck.set_appearance_mode("dark")
ck.set_default_color_theme("green")

# Create the main window
win = ck.CTk()
win.title("Password Manager")

# Set the size of the window
win.geometry("600x300")
def sth():
    
    lab1.configure(text="Hellowguys ")


but1=ck.CTkButton(win,text="Close the application", command=sth, corner_radius=25,font=("Buttermilk",15),height=50,width=30)
but1.pack(side=LEFT)

lab1=ck.CTkLabel(win,text="")
lab1.pack(side=LEFT)

# Start the main loop to display the window
win.mainloop()
