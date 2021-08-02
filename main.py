import os
import password # gets variables from the other files
import tkinter as tk
from tkinter import filedialog,Text



def dirfunc(x):
    os.chdir(x)

def killcontrolstrip():
    label = tk.Label(frame,text="loppa",bg="white")
    label.pack()

def openfiles():
   dirfunc(x='/Users/devan')  # pass the parameter of what you want inside
   opendir = "downloads" # pass what folder you want to open
   os.system("open "+opendir) 

root =  tk.Tk() # creation of gui

canvas = tk.Canvas(root, height=700, width=700,bg="#d8dee9") # styling
canvas.pack()# packaging the styling

frame = tk.Frame(root,bg="#88c0d0")
frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)

killercont=tk.Button(frame, text="KILLLER",padx=10,pady=5,fg="#bf616a",bg="#2e3440",command=killcontrolstrip)
killercont.pack()

openfile=tk.Button(frame, text="OPEN FILES",padx=10,pady=5,fg="#bf616a",bg="#2e3440",command=openfiles)
openfile.pack()

openf=tk.Button(root, text="Close",padx=10,pady=5,fg="#bf616a",bg="#2e3440")
openf.pack()


root.mainloop() # this runs the script



print("\n------------------\n completed \n ------------------")
