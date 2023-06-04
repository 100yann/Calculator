import customtkinter as ctk
from buttons import Buttons
from tkinter import *


display_expression = ''
total_expression = ''
LARGE_FONT=('Arial', 50)
SMALL_FONT=('Arial', 25)

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

# displays previous operations
secondary_display = ctk.CTkLabel(app,
                                 width=335, height=25,
                                 text='',
                                 anchor='se',
                                 font=SMALL_FONT)
secondary_display.pack(pady=5)

# label to display current display_expression
main_display = ctk.CTkLabel(app, 
                            width=335, height=125, 
                            text='0', 
                            anchor='se',
                            font=LARGE_FONT)
main_display.pack(pady=15)


# canvas for the calculator buttons
frame = ctk.CTkFrame(app, width=600, height=600)
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
    global display_expression, total_expression
    total_expression += f' {operator} ' 
    display_expression += f' {operator} '
    secondary_display.configure(text=total_expression)
    display_expression = ''

def equals():
    clearDisplay()
    global display_expression, total_expression
    result = eval(total_expression)
    result = round(result, 12)
    main_display.configure(text=result)

    display_expression = total_expression + ' ='
    secondary_display.configure(text=display_expression)
    display_expression = ''

def clearAll():
    clearDisplay()
    global total_expression, display_expression
    total_expression = ''
    display_expression = ''
    main_display.configure(text=0)
    secondary_display.configure(text='')


multiply_button = Buttons(frame, '*', lambda: getOperator('*'), row=0, column=4)
divide_button = Buttons(frame, '÷', lambda: getOperator('/'), row=1, column=4)
minus_button = Buttons(frame, '-', lambda: getOperator('-'), row=2, column=4)
plus_button = Buttons(frame, '+', lambda: getOperator('+'), row=3, column=4)
equals_button = Buttons(frame, '=', equals, row=4, column=4)
clear_button = Buttons(frame, 'CE', clearAll, row=0, column=3)


for index, i in enumerate(NUMBERS):
    digit_button = Buttons(frame, f'{index}', command= lambda x=index: getNum(x), row=i[0], column=i[1])



app.mainloop()