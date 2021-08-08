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
    global frame
    print("\napp has been closed")
    frame.destroy()

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

frame = tk.Frame(root,bg="#2e3440")
frame.pack()
# frame.place(relwidth=0.8,relheight=0.8)

# setting columns up
frame.columnconfigure(0,weight = 1)
frame.columnconfigure(1,weight = 1)
frame.columnconfigure(2,weight = 1)
frame.columnconfigure(3,weight = 1)
frame.columnconfigure(4,weight = 1)
frame.columnconfigure(5,weight = 1)
frame.columnconfigure(6,weight = 1)

# setting rows up, add multiple rows to the number of buttons wanted
frame.rowconfigure(0, weight = 2)
frame.rowconfigure(1, weight = 5)
frame.rowconfigure(2, weight = 5)
frame.rowconfigure(3, weight = 5)
frame.rowconfigure(4, weight = 5)
frame.rowconfigure(5, weight = 5)


# setting up root frames and rows
root.columnconfigure(1, weight = 1)
root.columnconfigure(2, weight = 1)
root.columnconfigure(3, weight = 1)

root.rowconfigure(0, weight = 1)

#pictures
###################### got to make the buttons smaller so they fit in a 1-1 row/col weight
offtoggle = tk.PhotoImage(file="button_red.png")
ontoggle = tk.PhotoImage(file="button_green.png")



# setting up layout
# canvas = tk.Canvas(frame, height=700, width=700,bg="#d8dee9") # styling
# canvas.pack(side = tk.TOP, fill = tk.BOTH, expand = True)# packaging the styling




# ############# chaning all the the frames to frames to test grid system
# text box suff
message = ""
abovetext = tk.Label(frame,text="\nEnter The Word That You Would Like \nTo Add To The Personal Dictionary Below\n", padx=10,pady=10,fg="#bf616a",bg="#2e3440")
abovetext.grid(column = 0, row = 0, sticky = tk.NW)

text_box = Text(
    frame,
    height=2,
    width=10,
    wrap='word',
    fg="#bf616a",
    bg="#2e3440"
)
text_box.grid(column = 1, row = 0, sticky = tk.NSEW, columnspan = 4)
text_box.insert('end', message)

# buttons!!!

#  add the option below or next to it asking the user if they want to save file auto aswell, 
#  so i dont auto save everything and hove to fix it later
#  keep this on dont save by or make the thing a bool so i can change the defualt value is wanted
opendic = tk.Button(frame, text="Auto Add to Personal Dictionary",padx=30,pady=10,fg="#bf616a",bg="#2e3440",command=auto_dic)
opendic.grid(column = 0, row = 1, sticky = tk.NSEW)

mandic = tk.Button(frame, text="Manually Add to Dictionary",padx=30,pady=10,fg="#bf616a",bg="#2e3440",command=opendicfunc)
mandic.grid(column = 1, row = 1, sticky = tk.NSEW)


#  seperation rows
# empty rows 
emptylabel = tk.Label(frame, text="\n-\nö",fg="#bf616a",bg="#2e3440")
emptylabel.grid(column=0, row=2, columnspan = 6, sticky = tk.NSEW)




# open file stuff
openfile=tk.Button(frame, text="Open Apps",padx=40,pady=20,fg="#bf616a",bg="#2e3440",command=openapps)
openfile.grid(column = 0, row = 3, sticky = tk.NSEW, columnspan  = 2)

#  i put an emoji in the label so it will look weird on none mac users
octallabel = tk.Label(frame, text="Open Octal? ➡️",fg="#bf616a",bg="#2e3440")
octallabel.grid(column = 0, row = 4, sticky = tk.NSEW)
addOctal=tk.Button(frame, text="Open Octal",padx=2.5,pady=2.5,image=offtoggle,command=switch_for_octal,fg="#bf616a",bg="#2e3440")
addOctal.grid(column = 1, row = 4, sticky = tk.NW)


# root buttons
# closetk=tk.Button(root, text="Close",padx=10,pady=5,fg="#bf616a",bg="#2e3440",command=tkclose)
# closetk.grid()



root.mainloop() # this runs the script

print("\n------------------\n completed \n ------------------")
