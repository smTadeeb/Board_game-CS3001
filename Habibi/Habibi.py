from tkinter import *
import tkinter .messagebox

myInterface = Tk()                        

myInterface.minsize(500,500)                                                   ##########################################                      
myInterface.maxsize(700,698)                                                   ## Defining max. and mi. size of canvas ## 
                                                                               ##########################################
                                          
label_info = Label(text="Habibi (حبيبي)Time pass",font= "Calibri 18 bold", bg = "orange" ,fg = "green")    ## Defined label of canvas
label_info.pack(side =TOP , anchor = "n" ,fill= X)

myInterface.title("Tadeeb's GUI")                                                       ## Defined title of canvas

f1 = Frame(myInterface,borderwidth = 5 ,bg= "goldenrod", relief = GROOVE)         ####################################### 
f1.pack(side = BOTTOM, anchor = "s" , fill = X)                                   ##                                   ## 
                                                                                  ##      Defined frame as pannels     ## 
f2 = Frame(myInterface,borderwidth = 2 ,bg= "goldenrod", relief = GROOVE)         ##                                   ##        
f2.pack(side = LEFT, anchor = "e" , fill = Y)                                     #######################################
 
                                                                      
L1 = Label(f2 , text = "grid size\n\
           \n10*10 ",bg = "goldenrod",font="Calibri 14 bold italic",)                   ## Defined label inside frame
L1.pack(side = LEFT , anchor = "w" ,fill= Y)

L2 = Label(f1, text="Player1:- Habibi digit 2",font="Calibri 14 bold italic",bg = "goldenrod" )
L2.pack( side = TOP , anchor = "s" ,fill= X,pady=3,padx=3)

L3 = Label(f1, text="Player2:- Habibi digit 3",font="Calibri 14 bold italic",bg = "goldenrod" )
L3.pack( side = TOP , anchor = "s" ,fill= X,pady=3,padx=3)

can_widget = Canvas(myInterface, width=500, height=500, background= "gold")       # Created Canvas         
can_widget.pack(fill = Y)

can_widget.create_line(0,5,500,5,fill = "black",width = 4)                       #####################################
can_widget.create_line(5,5,5,500,fill = "black",width = 4)                       ##                                 ##
can_widget.create_line(5,500,500,500,fill = "black",width = 4)                   ## Created canvas(GUI) and Borders ##
can_widget.create_line(500,5,500,500,fill = "black",width = 4)                   ##                                 ##
                                                                                 #####################################
                                                                                 
def close_window():
    """
    Asks the user if they really want to exit
    """
    if tkinter.messagebox.askokcancel("Exit", "Do you really wish to Exit?"):
        myInterface.destroy()
   

def game_rules():
    """
    Displays game rules
    """
    messagebox.showinfo("Game Rules" , "1. It is traditionally played with Habibi Digits (2 and 3) on a 20×20 or 10×10 Habibi board.\n\
                        \n2. Players alternatively place a digit assigned to them (either 2 or 3) on an cell.\n\
                        \n3. The winner is the first player to form an unbroken chain of five digits horizontally, vertically, or diagonally to get a sum of (10 or 15) depending upon his chosen number.\n\
                        \n4. So both the players should try to place their number in such a manner that their opponent aren’t able to make 5 digits in a row,column or diagonally.")
  
def checkered(canvas, line_distance):  
    """
    Used to make the 10*10 grid on canvas
    """
                                                                                           ########################################################
    for x in range(line_distance,500,line_distance):                                       ##                                                    ##
       canvas.create_line(x, 0, x, 500)                                                    ## Vertical lines at an interval of "line_distance"   ##
                                                                                           ## Horizontal lines at an interval of "line_distance" ##
    for y in range(line_distance,500,line_distance):                                       ##                                                    ##
       canvas.create_line(0, y, 500, y)                                                    ########################################################                                                      
                                                                              

    
    
b1 = Button(f1,fg="red",text="Exit",padx = "8",pady = "8",command = close_window)        #################################################################
b1.pack(side = TOP ,anchor ="s")                                                         ##                                                             ##
                                                                                         ## Buttons on canvas to exit,restart and to check game rules.  ##                 
b2 = Button(f1,fg="Green",text="Restart",padx = "8",pady = "8")                          ##                                                             ##
b2.pack(side = RIGHT ,anchor = "se" )                                                    #################################################################

b3 = Button(f1,fg="Blue",text="How to Play",padx = "5",pady = "5",command = game_rules)
b3.pack(side = LEFT ,anchor = "sw" )


checkered(can_widget,50)
myInterface.mainloop()



