import customtkinter as ctk

class Buttons:
    def __init__(self, master, text, command, row, column):
        self.button = ctk.CTkButton(master, 
                                    width=55, 
                                    height=35,
                                    text=text,
                                    command=command,
                                    font=('Arial', 25),
                                    corner_radius=5
                                    )
        self.button.grid(row=row, column=column, padx=0, pady=0)