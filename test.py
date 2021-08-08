import tkinter as tk

root = tk.Tk()
root.title("Test Grid")



root.columnconfigure(0,weight = 1)
root.columnconfigure(1,weight = 1)
root.columnconfigure(2,weight = 1)
root.columnconfigure(3,weight = 1)
root.columnconfigure(4,weight = 1)
root.columnconfigure(5,weight = 1)

root.rowconfigure(0, weight = 1)
root.rowconfigure(1, weight = 1)
root.rowconfigure(2, weight = 1)
root.rowconfigure(3, weight = 1)
root.rowconfigure(4, weight = 1)
root.rowconfigure(5, weight = 1)



col1lab = tk.Label(root, text = "banananannanana", bg = "#000", fg="#fff")
col1lab.grid(column = 0, row = 0, sticky = tk.W)

col2lab = tk.Label(root, text = "banananannanana", bg="#444", fg="#101010")
col2lab.grid(column = 1, row = 1, sticky = tk.W, columnspan = 2)

root.mainloop()