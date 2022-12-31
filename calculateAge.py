# importing the  tkinter module
from tkinter import*

# importing data class from datetime module
from datetime import date

# initializing tkinter
root = Tk()

# setting the width and height of GUI
root.geometry("700x500")

# setting the title of gui
root.title("Age Calculator")

# loading image
photo = PhotoImage(file= "C:\\Users\\user\\OneDrive\\Pictures\\photo_2022-02-20_13-20-471.png")

# creating a lable to show load image
myimage = Label(image= photo)

# placing the image label widget using grid method
myimage.grid(row=0, column=1)

# 
