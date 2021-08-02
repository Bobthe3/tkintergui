# import password # GET THE PASSWORDS FORM THE OTHER FILE
# from applescript import tell
# import applescript

# #set what command you want to run here
# yourCommand = 'ls'

# applescript.tell.app("Terminal",'do script "ls"',background=False)

# import appscript

# appscript.app('Terminal').do_script('sudo killall "ControlStrip";')

import os
import password # from the password storer
import tkinter as tk
from tkinter import filedialog,Text
import time

def killcontrolstrip():
    label = tk.Label(frame,text="loppa",bg="white")
    label.pack()

def openfiles():
    os.system("open ~")
    os.system("open Downloads")

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



print("\n------------------\n completed, gracias \n ------------------")
