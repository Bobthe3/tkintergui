# picture testing

# from tkinter import *
# import os


# def tkclose():
#     global root
#     print("\napp has been closed")
#     root.destroy()


# def opendic():
#     os.system('cd /Users/devan;cd Library/Spelling;open LocalDictionary')

# # Create Tkinter Object
# root = Tk()
 

# qwer = Button(root, text="dic",padx=10,pady=10,fg="#bf616a",bg="#2e3440",command=opendic)
# qwer.pack()

# closetk=Button(root, text="Close",padx=10,pady=5,fg="#bf616a",bg="#2e3440",command=tkclose)
# closetk.pack()



# root.mainloop()


#######################


f = open("myfile.txt", "a")
f.write("Now the file has more content!\n")
f.close()

#open and read the file after the appending:
f = open("myfile.txt", "r")
print(f.read()) 