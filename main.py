import os
import tkinter as tk
from tkinter import filedialog,Text

mainapplist = ['Firefox.app','Notion.app']
addapps = []
#default = False # can change this to true


def dirfunc(x):
    os.chdir(x)

def killcontrolstrip():
    label = tk.Label(frame,text="loppa",bg="white")
    label.pack()

def openapps():
   dirfunc(x='/')  # pass the parameter of what you want inside
   for a in mainapplist:
    os.system("open Applications/"+a)
   if len(addapps)!=0:
        for b in addapps:
            os.system("open Applications/"+b)
   

def switch_for_octal():
    global addapps
    on = 
    if on == True:
        addOctal.config(image=ontoggle,text="Octal Added")
        addapps=['Octal.app']
        on = False
        return addapps
    else:
        addOctal.config(image=offtoggle,text="Open Octal?")
        

root =  tk.Tk() # creation of gui

canvas = tk.Canvas(root, height=700, width=700,bg="#d8dee9") # styling
canvas.pack()# packaging the styling

frame = tk.Frame(root,bg="#88c0d0")
frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)

killercont=tk.Button(frame, text="KILLLER",padx=10,pady=10,fg="#bf616a",bg="#2e3440",command=killcontrolstrip)
killercont.pack()

openfile=tk.Button(frame, text="OPEN FILES",padx=40,pady=20,fg="#bf616a",bg="#2e3440",command=openapps)
openfile.pack()

offtoggle = tk.PhotoImage(file="toggle(1).png")
ontoggle = tk.PhotoImage(file="toggle(2).png")


addOctal=tk.Button(frame, text="Open Octal",padx=2.5,pady=2.5,image=offtoggle,command=switch_for_octal)
addOctal.pack()

closetk=tk.Button(root, text="OPEN FILES",padx=40,pady=20,fg="#bf616a",bg="#2e3440",command=tkclose)
closetk.pack()

root.mainloop() # this runs the script


print("\n------------------\n completed \n ------------------")
