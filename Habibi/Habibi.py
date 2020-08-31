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
L1 = Label(f2 , text = "grid size"\n\
           10*10 ")
L1.pack()

can_widget = Canvas(myInterface, width=600, height=600, background= "gold")          
can_widget.pack(fill = BOTH)

can_widget.create_line(0,5,600,5,fill = "black",width = 4)
can_widget.create_line(5,5,5,600,fill = "black",width = 4)
can_widget.create_line(5,600,600,600,fill = "black",width = 4)
can_widget.create_line(600,5,600,600,fill = "black",width = 4)
           
def close_window():
    myInterface.destroy()
 
def game_rules():
    messagebox.showinfo("Game Rules" , "1. It is traditionally played with Habibi Digits (2 and 3) on a 20×20 or 10×10 Habibi board.\n\
                        \n2. Players alternatively place a digit assigned to them (either 2 or 3) on an cell.\n\
                        \n3. The winner is the first player to form an unbroken chain of five digits horizontally, vertically, or diagonally to get a sum of (10 or 15) depending upon his chosen number.\n\
                        \n4. So both the players should try to place their number in such a manner that their opponent aren’t able to make 5 digits in a row,column or diagonally.")
     
           
b1 = Button(f1,fg="red",text="Exit",command = close_window)
b1.pack(side = BOTTOM ,anchor ="se")

b2 = Button(f1,fg="Green",text="Restart")
b2.pack(side = RIGHT,anchor = "se" )

b3 = Button(f1,fg="Blue",text="How to Play",padx = "5",pady = "5",command = game_rules)
b3.pack(side = LEFT ,anchor = "sw" )

def checkered(canvas, line_distance):
   # vertical lines at an interval of "line_distance" 
   for x in range(line_distance,600,line_distance):
      canvas.create_line(x, 0, x, 600)
   # horizontal lines at an interval of "line_distance" 
   for y in range(line_distance,600,line_distance):
      canvas.create_line(0, y, 600, y)
           

checkered(can_widget,60)
myInterface.mainloop()
