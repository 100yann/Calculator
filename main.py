import customtkinter as ctk
from buttons import Buttons
from tkinter import *


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


# canvas for the calculator buttons
frame = ctk.CTkFrame(app, width=350, height=600)
frame.pack()


expression = ''
def getNum(num):
    global expression
    expression += str(num)
    print(expression)


multiply_button = Buttons(frame, '*', lambda: calculate(entry_num.get(), '*'), row=0, column=4)
divide_button = Buttons(frame, '÷', lambda: calculate(entry_num.get(), '/'), row=1, column=4)
minus_button = Buttons(frame, '-', lambda: calculate(entry_num.get(), '-'), row=2, column=4)
plus_button = Buttons(frame, '+', lambda: calculate(entry_num.get(), '+'), row=3, column=4)
equals_button = Buttons(frame, '=', lambda: equals(entry_num.get()), row=4, column=4)

for index, i in enumerate(NUMBERS):
    digit_button = Buttons(frame, f'{index}', command= lambda x=index: getNum(x), row=i[0], column=i[1])



app.mainloop()