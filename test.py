# picture testing

from tkinter import *
from PIL import Image, ImageTk
 
# Create Tkinter Object
root = Tk()
 
# Read the Image
image = Image.open("toggle(1).png").resize((40, 40))
img12 = ImageTk.PhotoImage(image)
label2 = Label(image=img12).pack()



# Reszie the image using resize() method
# resize_image = image.resize((40, 40))
# img = ImageTk.PhotoImage(resize_image)
# label1 = Label(image=img).pack()
 
# Execute Tkinter
root.mainloop()