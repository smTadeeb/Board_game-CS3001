from tkinter import *

myInterface = Tk()
myInterface.minsize(600,600)
myInterface.maxsize(900,900)

label_info = Label(text="Habibi (حبيبي)Time pass",font= "Calibri 12 bold",fg = "green")
label_info.pack(side =TOP , anchor = "n" ,fill= X)

myInterface.title("Tadeeb's GUI")

f1 = Frame(myInterface,borderwidth = 5 ,bg= "goldenrod", relief = GROOVE)
f1.pack(side = BOTTOM, anchor = "s" , fill = X)

f2 = Frame(myInterface,borderwidth = 8 ,bg= "goldenrod", relief = GROOVE)
f2.pack(side = LEFT, anchor = "e" , fill = Y)
L1 = Label(f2 , text = "grid size")
L1.pack()

def close_window():
    myInterface.destroy()
b1 = Button(f1,fg="red",text="Exit",command = close_window)
b1.pack(side = BOTTOM ,anchor ="se")

b2 = Button(f1,fg="Green",text="Restart")
b2.pack(side = RIGHT,anchor = "se" )

b3 = Button(f1,fg="Blue",text="How to Play",padx = "5",pady = "5")
b3.pack(side = LEFT ,anchor = "sw" )


myInterface.mainloop()
