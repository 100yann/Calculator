import customtkinter as ctk


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


# canvas for the calculator buttons and entry
frame = ctk.CTkFrame(app, width=350, height=500)
frame.pack()

# create entry
num = ctk.CTkEntry(frame, width=300, height=100, font=('Arial', 40), placeholder_text=0, justify='right')
app.after(1, lambda: num.focus())
num.grid(row=0, column=0, columnspan=1)




app.mainloop()