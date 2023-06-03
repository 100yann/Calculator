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
dark_or_light.grid(row=0, column=1)






app.mainloop()