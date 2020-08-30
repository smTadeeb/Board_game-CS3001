from tkinter import *
from time import *
import sys

myInterface = Tk()
myInterface.minsize(600,600)
myInterface.maxsize(900,900)

label_info = Label(text="Habibi (حبيبي)Time pass",font= "Calibri 12 bold",fg = "green")
label_info.pack(side =TOP , anchor = "n" ,fill= X)

myInterface.title("Tadeeb's GUI")

f1 = Frame(myInterface,borderwidth = 8 ,bg= "gold", relief = SUNKEN)
f1.pack(side = BOTTOM, anchor = "s" , fill = X)

#Photo = PhotoImage(file="Habibi.png") 
#Photo_label = Label(image= Photo)
#Photo_label.pack()

#s = Canvas(myInterface, width=600, height=600, background= "gold")          
#s.pack(fill = X)

b1 = Button(f1,fg="red",text="Exit")
b1.pack(side = BOTTOM ,anchor ="se")

b2 = Button(f1,fg="Green",text="Restart")
b2.pack(side = BOTTOM,anchor = "se" )

myInterface.mainloop()
