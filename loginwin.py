import tkinter
import customtkinter as ck
from constant import *
from PIL import ImageTk, Image

# Default appearance
ck.set_appearance_mode("dark")
ck.set_default_color_theme("green")

# Creating login window
login = ck.CTk()
login.title("Login Page")
login.geometry(f"{WIDTH}x{HEIGHT}")

# Open the image and create a label for background
img1 = ImageTk.PhotoImage(Image.open("pattern.png"))
lab1 = ck.CTkLabel(master=login, image=img1)
lab1.pack(fill="both", expand=True)

# Login Page title
titlelab = ck.CTkLabel(master=login, text="Welcome to sasta pr sabse acha password manager", font=("Comic Sans MS", 32, "italic"))
titlelab.place(x=50, y=45)

# Frame for subsection of login page (the rectangle in the main window)
loginframe = ck.CTkFrame(master=lab1, width=350, height=380, corner_radius=25)
loginframe.place(relx=0.5, y=(45+80), anchor=tkinter.N)
t2=ck.CTkLabel(master=loginframe,text="Log in",font=("Verdana",25,"bold"))
t2.place(relx=0.5,rely=0.1,anchor=tkinter.CENTER)

entry1=ck.CTkEntry(master=loginframe,width=250,placeholder_text="Enter username",corner_radius=25)
entry1.place(x=50,y=110)

entry2=ck.CTkEntry(master=loginframe,width=250,placeholder_text="Enter the password",corner_radius=25)
entry2.place(x=50,y=180)

LoginButt=ck.CTkButton(master=loginframe,width=220,text="Login",corner_radius=50)
LoginButt.place(x=60,y=250)
prif()
# Looping the login window
login.mainloop()
prif()