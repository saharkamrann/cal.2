import tkinter as tk 
calculation = ''
#======================================================COMMANDS=============================================
def clear_field():
    global calculation
    calculation = ''
    text_result.delete(1.0 , 'end')

def add_to_calculation(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0 , 'end')
    text_result.insert(1.0 , calculation)

def evaluate_calculation():
    global calculation
    try:
        calculation = str(eval(calculation))
        text_result.delete(1.0 , 'end')
        text_result.insert(1.0 , calculation)
    except:
        clear_field()
        text_result.insert(1.0 , 'error')
        

def add_percent():
    global calculation
    calculation=str(int(calculation)*(1/100))
    text_result.delete(1.0 , 'end')
    text_result.insert(1.0,calculation)

#======================================================================MAIN WINDOW==================================================================

window = tk.Tk()
window.title('calculator')
window.geometry('300x275')
text_result = tk.Text(window , height=2 , width=16 , font=('arial' , 24))
text_result.grid(columnspan=5)

#========================================================================NUMBER BUTTONS====================================================================

btn1 = tk.Button(window , text="1" ,background="white" ,command=lambda: add_to_calculation(1) , width=5 , font=('Arial' , 14)).grid(row=4 , column=1)
btn2 = tk.Button(window , text='2' , background="white",command=lambda:  add_to_calculation(2), width=5 , font=('Arial' , 14)).grid(row=4 , column=2)
btn3 = tk.Button(window , text='3' ,background="white" ,command=lambda:  add_to_calculation(3), width=5 , font=('Arial' , 14)).grid(row=4 , column=3)
btn4 = tk.Button(window , text='4' , background="white",command=lambda:  add_to_calculation(4), width=5 , font=('Arial' , 14)).grid(row=3 , column=1)
btn5 = tk.Button(window , text='5' ,background="white" ,command=lambda:  add_to_calculation(5), width=5 , font=('Arial' , 14)).grid(row=3 , column=2)
btn6 = tk.Button(window , text='6' ,background="white" ,command=lambda:  add_to_calculation(6), width=5 , font=('Arial' , 14)).grid(row=3 , column=3)
btn7 = tk.Button(window , text='7' ,background="white" ,command=lambda:  add_to_calculation(7), width=5 , font=('Arial' , 14)).grid(row=2 , column=1)
btn8 = tk.Button(window ,text='8' ,background="white" ,command=lambda:  add_to_calculation(8), width=5 , font=('Arial' , 14)).grid(row=2 , column=2)
btn9 = tk.Button(window ,  text='9' ,background="white" ,command=lambda:  add_to_calculation(9), width=5 , font=('Arial' , 14)).grid(row=2 , column=3)
btn0 = tk.Button(window ,  text='0' ,background="white" ,command=lambda:  add_to_calculation(0), width=5 , font=('Arial' , 14)).grid(row=5 , column=2)

#=======================================================================ACTION BUTTONS======================================================================

btn_plus = tk.Button(window  , background="green", text='+' , command=lambda:  add_to_calculation('+'), width=5 , font=('Arial' , 14)).grid(row=5 , column=4)
btn_minus = tk.Button(window , text='-' ,  background="sky blue",command=lambda:  add_to_calculation('-'), width=5 , font=('Arial' , 14)).grid(row=4 , column=4)
btn_mul = tk.Button(window , text='*' ,  background="gold",command=lambda:  add_to_calculation('*'), width=5 , font=('Arial' , 14)).grid(row=3 , column=4)
btn_div = tk.Button(window , text='/' ,  background="orange",command=lambda:  add_to_calculation('/'), width=5 , font=('Arial' , 14)).grid(row=2 , column=4)
btn_open = tk.Button(window , text='(', background="gray" ,command=lambda:  add_to_calculation('('), width=5 , font=('Arial' , 14)).grid(row=5 , column=1)
btn_close = tk.Button(window , text=')', background="gray" ,command=lambda:  add_to_calculation(')'), width=5 , font=('Arial' , 14)).grid(row=5 , column=3)
btn_point = tk.Button(window , text='.' , background="pink",command=lambda:  add_to_calculation('.'), width=5 , font=('Arial' , 14)).grid(row=6 , column=2)

#========================================================================COMMAND BUTTONS====================================================================

btn_equals = tk.Button(window , text='=' , background="black" ,foreground="white",command= evaluate_calculation, width=5 , font=('Arial' , 14)).grid(row=6 , column=4 , columnspan=2)
btn_clear = tk.Button(window ,  background="red", text='c' , command=clear_field , width=5 , font=('Arial' , 14)).grid(row=6 , column=1  )
btn_percent = tk.Button(window , text='%' ,background="purple" , command= add_percent, width=5 , font=('Arial' , 14)).grid(row=6 , column=3)

window.resizable(0, 0)
window.mainloop()