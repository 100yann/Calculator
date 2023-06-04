import customtkinter as ctk

class Buttons:
    def __init__(self, master, text, command, row, column):
        self.button = ctk.CTkButton(master, 
                                    width=85, 
                                    height=75,
                                    text=text,
                                    command=command,
                                    font=('Arial', 25),
                                    corner_radius=5,
                                    fg_color='gray20',
                                    text_color='gray90',
                                    hover_color='gray30',
                                    bg_color='transparent'
                                    )
        self.button.grid(row=row, column=column, padx=1, pady=1)