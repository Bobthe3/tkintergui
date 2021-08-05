import os
import tkinter as tk
from tkinter import filedialog,Text
from PIL import Image, ImageTk


mainapplist = []
addapps = []

#default = False # can change this to true


def tkclose():
    global root
    print("\napp has been closed")
    root.destroy()

def dirfunc(x):
    os.chdir(x)
    print("----------------changed dir")

def killcontrolstrip():
    label = tk.Label(frame,text="loppa",bg="white").pack()
    print("labeled loppa\n")

def openapps():
   dirfunc(x='/') # pass the parameter of what you want inside
   if len(mainapplist) == 0:
       ("no main apps")

   if len(addapps) == 0:
       print("no add apps")

   if len(mainapplist)!=0:
    for a in mainapplist:
        os.system("open Applications/"+a)
    print(("for first loop"))

   if len(addapps)!=0:
        for b in addapps:
            os.system("open Applications/"+b)
        print("inside not loop")
   
octalswitchcase = 0
def switch_for_octal():
    global addapps, octalswitchcase

    if (octalswitchcase % 2) == 0:
        addOctal.config(image=ontoggle,text="Octal Added")
        addapps=['Octal.app']
        octalswitchcase += 1
        print(octalswitchcase)
        return addapps

    if (octalswitchcase % 2) !=0:
        addOctal.config(image=offtoggle,text="Open Octal?")
        octalcheck = "Octal.app" in addapps
        if octalcheck == True:
            addapps.remove("Octal.app")
            octallabel = tk.Label(frame,text=" Added Octal",bg="white").pack() # adds a label to the thing
        octalswitchcase += 1
        return addapps


root =  tk.Tk() # creation of gui

canvas = tk.Canvas(root, height=700, width=700,bg="#d8dee9") # styling
canvas.pack()# packaging the styling

frame = tk.Frame(root,bg="#88c0d0")
frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)

killercont=tk.Button(frame, text="KILLLER",padx=10,pady=10,fg="#bf616a",bg="#2e3440",command=killcontrolstrip)
killercont.pack()

openfile=tk.Button(frame, text="OPEN FILES",padx=40,pady=20,fg="#bf616a",bg="#2e3440",command=openapps)
openfile.pack()

# # setting image sizes 
# qwerty = Image.open("toggle(1).png").resize((40,40))
# offtoggle = tk.PhotoImage(qwerty)

# qwerty = Image.open("toggle(2).png").resize((40,40))
# ontoggle = tk.PhotoImage(qwerty)


offtoggle = tk.PhotoImage(file="button_red.png")
ontoggle = tk.PhotoImage(file="button_green.png")


addOctal=tk.Button(frame, text="Open Octal",padx=2.5,pady=2.5,image=offtoggle,command=switch_for_octal)
addOctal.pack()

closetk=tk.Button(root, text="Close",padx=10,pady=5,fg="#bf616a",bg="#2e3440",command=tkclose)
closetk.pack()

root.mainloop() # this runs the script


print("\n------------------\n completed \n ------------------")
