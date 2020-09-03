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
                                                                              
def restart_program():
    """Restarts the current program.
    Note: this function does not return. Any cleanup action (like
    saving data) must be done before calling this function."""
    python = sys.executable
    os.execl(python, python, * sys.argv)
    return restart_program()
                                                                                                                                   
b1 = Button(f1,fg="red",text="Exit",padx = "8",pady = "8",command = close_window)            #################################################################
b1.pack(side = TOP ,anchor ="s")                                                             ##                                                             ##
                                                                                             ## Buttons on canvas to exit,restart and to check game rules.  ##                 
b2 = Button(f1,fg="Green",text="Restart",padx = "8",pady = "8",,command = restart_program)   ##                                                             ##
b2.pack(side = RIGHT ,anchor = "se" )                                                        #################################################################

b3 = Button(f1,fg="Blue",text="How to Play",padx = "5",pady = "5",command = game_rules)
b3.pack(side = LEFT ,anchor = "sw" )


checkered(can_widget,50)

#Board Size
Board_Size = int(16.2)
Frame_Gap = 35
width = 500
height = 500

def create_circle(x, y, radius, fill = "", outline = "black", width = 1):
    can_widget.create_oval(x - radius, y - radius, x + radius, y + radius, fill = fill, outline = outline, width = width)       # Use for creating circles 

def Value_Check_int(Value):
    try:
        Value = int(Value)
    except ValueError:                   # Used to add functionalities to the program by click of mouse
        return "string"
    else:
        return "int"

def MouseClick(event):
    global Click_Cord
    X_click = event.x
    Y_click = event.y
    Click_Cord = Piece_Location(X_click, Y_click)
    print(Click_Cord)

can_widget.bind("<Button-1>", MouseClick)

Click_Cord = [None, None]

def Piece_Location(X_click, Y_click):               # Checks for the location/co-ordinate where the click has been made
    X = None                                          
    Y = None
    for i in range(len(Actual_CordX1)):
        
        if X_click > Actual_CordX1[i] and X_click < Actual_CordX2[i]:
            X = Game_CordX[i]

        if Y_click > Actual_CordY1[i] and Y_click < Actual_CordY2[i]:
            Y = Game_CordY[i]

    return X, Y

def Location_Validation():                                                     # Validates whether a block exist on a perticular place or not

    if X == None or Y == None:
        return False
        
    elif board[Y - 1][X - 1] == 0:
        return True

#Board
Board_Size = Board_Size - 1
Board_X1 = 500 / 10
Board_Y1 = 500 / 10
Board_GapX = (500 - Board_X1 * 2) / Board_Size
Board_GapY = (500 - Board_Y1 * 2) / Board_Size

#Chess Piece
Chess_Radius = (Board_GapX * (9 / 10)) / 2

#Cord List
Black_Cord_PickedX = []
Black_Cord_PickedY = []
White_Cord_PickedX = []
White_Cord_PickedY = []

#Click Detection Cord
Game_CordX = []
Game_CordY = []
Actual_CordX1 = []
Actual_CordY1 = []
Actual_CordX2 = []
Actual_CordY2 = []

#2D Board List
board = []

#2D list for gameboard
for i in range(Board_Size + 1):
    board.append([0] * (Board_Size + 1))
    
Unfilled = 0
Black_Piece = 1
White_Piece = 2

#Fills Empty List
for z in range(1, Board_Size + 2):
    
    for i in range(1, Board_Size + 2):
        Game_CordX.append(z)
        Game_CordY.append(i)
        Actual_CordX1.append((z - 1) * Board_GapX + Board_X1 - Chess_Radius)
        Actual_CordY1.append((i - 1) * Board_GapY + Board_Y1 - Chess_Radius)
        Actual_CordX2.append((z - 1) * Board_GapX + Board_X1 + Chess_Radius)
        Actual_CordY2.append((i - 1) * Board_GapY + Board_Y1 + Chess_Radius)
        
#Turn
Turn_Num = 1
Turn = "black"
Winner = None

#Game Code
while Winner == None:
    can_widget.update()

    X = Click_Cord[0]
    Y = Click_Cord[1]

    Picked = Location_Validation()

    if Picked:       
        create_circle(Board_X1 + Board_GapX * (X - 1), Board_Y1 + Board_GapY * (Y - 1), radius = Chess_Radius, fill = Turn)

        if Turn_Num % 2 == 1:
            White_Cord_PickedX.append(X)
            White_Cord_PickedY.append(Y)
            board[Y - 1][X - 1] = 2
            Turn = "black"

        elif Turn_Num % 2 == 0:
            Black_Cord_PickedX.append(X)
            Black_Cord_PickedY.append(Y)
            board[Y - 1][X - 1] = 1
            Turn = "white"
      
myInstance.mainloop()



