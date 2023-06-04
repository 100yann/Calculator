import customtkinter as ctk
from buttons import Buttons
from tkinter import *


display_expression = ''
total_expression = ''
LARGE_FONT=('Arial', 50)
NUMBERS = [
    [4, 2], 
    [3, 1], [3, 2], [3, 3],
    [2, 1], [2, 2], [2, 3],
    [1, 1], [1, 2], [1, 3],


]

# init the GUI
app = ctk.CTk()
app.geometry('400x600')
app.resizable(False, False)
app.title('Calculator')


# make it dark or light mode
def appearanceMode():
    if switch_var.get() == 'on':
        ctk.set_appearance_mode('dark')
    else:
        ctk.set_appearance_mode('light')


# dark or light mode switch
switch_var = ctk.StringVar(value='on')
dark_or_light = ctk.CTkSwitch(app, 
                              text='', 
                              command=appearanceMode, 
                              variable=switch_var,
                              onvalue='on',
                              offvalue='off',
                              )
dark_or_light.pack()


# label to display current display_expression
main_display = ctk.CTkLabel(app, 
                            width=250, height=125, 
                            text='0', 
                            anchor='se',
                            font=LARGE_FONT)
main_display.pack(pady=15)

# canvas for the calculator buttons
frame = ctk.CTkFrame(app, width=350, height=600)
frame.pack()


def clearDisplay():
    main_display.configure(text='')

def getNum(num):
    clearDisplay()
    global display_expression, total_expression
    display_expression += str(num)
    total_expression += str(num)
    main_display.configure(text=display_expression)

def getOperator(operator):
    clearDisplay()
    global display_expression, total_expression
    total_expression += operator
    display_expression = ''

def equals():
    clearDisplay()
    result = eval(total_expression)
    result = round(result, 12)
    main_display.configure(text=result)


multiply_button = Buttons(frame, '*', lambda: getOperator('*'), row=0, column=4)
divide_button = Buttons(frame, '÷', lambda: getOperator('/'), row=1, column=4)
minus_button = Buttons(frame, '-', lambda: getOperator('-'), row=2, column=4)
plus_button = Buttons(frame, '+', lambda: getOperator('+'), row=3, column=4)
equals_button = Buttons(frame, '=', equals, row=4, column=4)


for index, i in enumerate(NUMBERS):
    digit_button = Buttons(frame, f'{index}', command= lambda x=index: getNum(x), row=i[0], column=i[1])



app.mainloop()