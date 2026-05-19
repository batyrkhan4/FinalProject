import tkinter as tk

from ui.theme import DARK, LIGHT, BLUE
from ui.components import create_header, create_display, create_buttons
from core.actions import handle_click
from core.data import STANDARD, SCIENTIFIC, SCIENTIFIC_SECOND

class Calculator:

    def __init__(self,root):

        self.root=root
        self.mode="standard"
        self.second_mode=False
        self.saved_value=None
        self.waiting_log =False

        self.theme=DARK

        root.title("Calculator")
        root.geometry("430x760")
        root.configure(bg=self.theme["bg"])
        root.resizable(False,False)

        create_header(self)
        create_display(self)
        create_buttons(self)

    def load_buttons(self):

        buttons=STANDARD

        if self.mode=="scientific":

            buttons=(
                SCIENTIFIC_SECOND
                if self.second_mode
                else SCIENTIFIC
            )

        for r,row in enumerate(buttons):

            for c,text in enumerate(row):

                color=self.theme["button"]

                if text=="=":
                    color=self.theme["equal"]

                tk.Button(
                    self.frame,
                    text=text,
                    font=("Segoe UI",17),
                    bg=color,
                    fg=self.theme["text"],
                    bd=0,
                    command=lambda t=text:self.click(t)
                ).grid(
                    row=r,
                    column=c,
                    sticky="nsew",
                    padx=1,
                    pady=1,
                    ipadx=10,
                    ipady=18
                )

        for i in range(len(buttons)):
            self.frame.grid_rowconfigure(i,weight=1)

        for j in range(len(buttons[0])):
            self.frame.grid_columnconfigure(j,weight=1)

    def click(self,value):
        handle_click(self,value)

    def open_menu(self):

        self.mode=(
            "scientific"
            if self.mode=="standard"
            else "standard"
        )

        self.second_mode=False

        self.title.config(
            text=self.mode.title()
        )

        for x in self.frame.winfo_children():
            x.destroy()

        self.load_buttons()

    def open_history(self):
        print("history")

    def open_settings(self):

        win=tk.Toplevel(self.root)

        win.geometry("250x200")

        tk.Button(
            win,
            text="Dark",
            command=lambda:self.change_theme(DARK)
        ).pack(fill="x")

        tk.Button(
            win,
            text="Light",
            command=lambda:self.change_theme(LIGHT)
        ).pack(fill="x")

        tk.Button(
            win,
            text="Blue",
            command=lambda:self.change_theme(BLUE)
        ).pack(fill="x")

    def change_theme(self,theme):

        self.theme=theme

        self.root.configure(
            bg=self.theme["bg"]
        )

        create_header(self)
        create_display(self)
        create_buttons(self)