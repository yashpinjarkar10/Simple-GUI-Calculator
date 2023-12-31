from tkinter import*

win = Tk()
win.title("It_Calculator_baby")
win.geometry('370x365')
win.resizable(0,0)


#function to take inpute whenever button is click
def bt_click(item):
    global expression
    expression += str(item)
    input_text.set(expression)
    
    
#function to clear input feild

def bt_clear():
    global expression
    expression = ""
    input_text.set("")    

#function for equal button

def bt_equal():
    global expression
    try:
        result = "Ye le ans saale -->  " + str(eval(expression))
    except Exception:
        result = "Saale galat inpute hai"
    input_text.set(result)
    expression =""



expression = ""
input_text = StringVar()

input_frame = Frame(win , width= 270 , height= 50)
input_frame.pack(side= TOP )

input_feild = Entry(input_frame, font = ("arial",18, "bold"), width=38 , justify= RIGHT , textvariable=input_text)
input_feild.grid(row = 0 ,column=0)

#incresing heght  of input_feild
input_feild.pack( ipady=10, padx=10,pady=10)


#bottom frame creating
bt_frame = Frame(win , width= 270 , height= 270 )
bt_frame.pack()

clear = Button(bt_frame , text = "C" , width=35 , height= 3 ,  command = lambda: bt_clear()).grid(row= 0 , column= 0, columnspan= 3, padx =1 , pady = 1)

divide =Button(bt_frame ,text= "/" , width= 10 ,height= 3 , command = lambda: bt_click("/")).grid(row= 0 , column= 3 ,padx=1 , pady= 1)

#button secound row


seven =Button(bt_frame ,text= "7" , width= 10 ,height= 3, command = lambda: bt_click(7) ).grid(row= 1 , column= 0 ,padx=1 , pady= 1)
eight =Button(bt_frame ,text= "8" , width= 10 ,height= 3, command = lambda: bt_click(8) ).grid(row= 1 , column= 1 ,padx=1 , pady= 1)
nine  =Button(bt_frame ,text= "9" , width= 10 ,height= 3 , command = lambda: bt_click(9)).grid(row= 1 , column= 2 ,padx=1 , pady= 1)
mul   =Button(bt_frame ,text= "*" , width= 10 ,height= 3, command = lambda: bt_click("*") ).grid(row= 1 , column= 3 ,padx=1 , pady= 1)


#button third row

four =Button(bt_frame ,text= "4" , width= 10 ,height= 3, command = lambda: bt_click(4) ).grid(row= 2 , column= 0 ,padx=1 , pady= 1)
five =Button(bt_frame ,text= "5" , width= 10 ,height= 3 , command = lambda: bt_click(5)).grid(row= 2 , column= 1 ,padx=1 , pady= 1)
six  =Button(bt_frame ,text= "6" , width= 10 ,height= 3, command = lambda: bt_click(6) ).grid(row= 2 , column= 2 ,padx=1 , pady= 1)
minus=Button(bt_frame ,text= "-" , width= 10 ,height= 3, command = lambda: bt_click("-") ).grid(row= 2 , column= 3 ,padx=1 , pady= 1)

#button fourth row

one  =Button(bt_frame ,text= "1" , width= 10 ,height= 3 , command = lambda: bt_click(1)).grid(row= 3 , column= 0 ,padx=1 , pady= 1)
two  =Button(bt_frame ,text= "2" , width= 10 ,height= 3, command = lambda: bt_click(2) ).grid(row= 3 , column= 1 ,padx=1 , pady= 1)
three=Button(bt_frame ,text= "3" , width= 10 ,height= 3, command = lambda: bt_click(3) ).grid(row= 3 , column= 2 ,padx=1 , pady= 1)
plus =Button(bt_frame ,text= "+" , width= 10 ,height= 3, command = lambda: bt_click("+") ).grid(row= 3 , column= 3 ,padx=1 , pady= 1)

#button fifth row

zero   =Button(bt_frame ,text= "0" , width= 24 ,height= 3, command = lambda: bt_click(0) ).grid(row= 4 , column= 0 ,padx=1 ,columnspan=2 ,  pady= 1)
decimal=Button(bt_frame ,text= "." , width= 10 ,height= 3, command = lambda: bt_click(".") ).grid(row= 4 , column= 2,padx=1 , pady= 1)
equals =Button(bt_frame ,text= "=" , width= 10 ,height= 3 ,  command = lambda: bt_equal()).grid(row= 4 , column= 3 ,padx=1 , pady= 1 )




win.mainloop()
