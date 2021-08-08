import tkinter as tk

root = tk.Tk()
root.title("Test Grid")


# there doesnt need to be that many columns rows is more impotant
root.columnconfigure(0,weight = 1)
root.columnconfigure(1,weight = 5)
root.columnconfigure(2,weight = 1)

# add multiple rows as each line will need its own row
root.rowconfigure(0, weight = 1)
root.rowconfigure(1, weight = 5)
root.rowconfigure(2, weight = 5)

offtoggle = tk.PhotoImage(file="button_red.png")
ontoggle = tk.PhotoImage(file="button_green.png")


# for the addition to a row like a words then a button 
#  make the whole words and button on one row 
#   make the 2 diffrent objects diffrent columns
#   adjust the column width to properly allow the fitting of an image 
#  ig the geomertry does not need to be set before had because it will...
#       adjust on its own


# the rows start on the zeroth and go up so coding row = row - 1

# row 1
col1lab = tk.Label(root, text = "0,0", bg = "#000", fg="#fff")
col1lab.grid(column = 0, row = 0, sticky = tk.NW)


# row 2
col2lab = tk.Label(root, text = "0,1", bg="#444", fg="#101010")
col2lab.grid(column = 0, row = 1, sticky = tk.NW)

addOctal=tk.Button(root, text="Open Octal",padx=2.5,pady=2.5,image=offtoggle)
addOctal.grid(column = 1, row = 1, sticky = tk.NE)

#  row 3
col2lab = tk.Label(root, text = "0,2", bg="#444", fg="#101010")
col2lab.grid(column = 0, row = 2, sticky = tk.NW)

addOctal=tk.Button(root, text="Open Octal 2",padx=2.5,pady=2.5,image=offtoggle)
addOctal.grid(column = 1, row = 2, sticky = tk.NE)

root.mainloop()