import os
import tkinter as tk
from tkinter import filedialog,Text
from PIL import Image, ImageTk
import pyautogui as pag
import time

###################################

mainapplist = []
addapps = []

pag.FAILSAFE = True

###################

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
    # func adds octal to the open apps 
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

def opendicfunc():
    # func just opesn the local dic
    os.system('cd /Users/devan;cd Library/Spelling;open LocalDictionary')
    
def auto_dic():
    # func does the auto dic and add word from text box
    print(text_box.get('1.0', 'end'))
    textentered = text_box.get('1.0', 'end')
    
    #opening the file
    os.system('cd /Users/devan;cd Library/Spelling;open LocalDictionary')

    pag.moveTo(770,420,duration=1)
    pag.click(770, 420,duration=1)
    pag.typewrite(["enter"])
    pag.typewrite(textentered)
    time.sleep(1)
    print("\n-------text entered\n")
    pag.click(156, 77)
    pag.hotkey("ctrl","s")
    pag.click(473,326)
    print("______done________")




##################################################################


root =  tk.Tk() # creation of gui
root.title("Magic Controller")

#root rows weight

# root.rowconfigure(0,weigth=1)


#pictures
offtoggle = tk.PhotoImage(file="button_red.png")
ontoggle = tk.PhotoImage(file="button_green.png")



# setting up layout
canvas = tk.Canvas(root, height=700, width=700,bg="#d8dee9") # styling
canvas.pack()# packaging the styling

frame = tk.Frame(root,bg="#88c0d0")
frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)


# text box suff
message = ""
abovetext = tk.Label(frame,text="Enter The Word That You Would Like To Add To The Personal Dictionary Below", padx=10,pady=10,fg="#bf616a",bg="#2e3440")
abovetext.pack()

text_box = Text(
    frame,
    height=13,
    width=40,
    wrap='word'
)
text_box.pack(expand=True)
text_box.insert('end', message)

# buttons
opendic = tk.Button(frame, text="Auto Personal Dictionary",padx=30,pady=10,fg="#bf616a",bg="#2e3440",command=auto_dic)
opendic.pack()

mandic = tk.Button(frame, text="Manual Personal Dictionary",padx=30,pady=10,fg="#bf616a",bg="#2e3440",command=opendicfunc)
mandic.pack()

openfile=tk.Button(frame, text="Open Apps",padx=40,pady=20,fg="#bf616a",bg="#2e3440",command=openapps)
openfile.pack()

addOctal=tk.Button(frame, text="Open Octal",padx=2.5,pady=2.5,image=offtoggle,command=switch_for_octal)
addOctal.pack()


# root buttons
closetk=tk.Button(root, text="Close",padx=10,pady=5,fg="#bf616a",bg="#2e3440",command=tkclose)
closetk.pack()



root.mainloop() # this runs the script

print("\n------------------\n completed \n ------------------")
