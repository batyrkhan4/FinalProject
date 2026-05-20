import tkinter as tk

from storage.history import load_history, clear_all_history, history_generator
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

    def open_history(self):

        history_window = tk.Toplevel(self.root)
        history_window.title("Calculation History")
        history_window.geometry("500x400")
        history_window.configure(bg=self.theme["bg"])

        title = tk.Label(
            history_window,
            text="Calculation History",
            font=("Segoe UI", 18, "bold"),
            bg=self.theme["bg"],
            fg=self.theme["text"]
        )
        title.pack(pady=10)

        history_box = tk.Text(
            history_window,
            font=("Segoe UI", 12),
            bg=self.theme["display_bg"] if "display_bg" in self.theme else self.theme["bg"],
            fg=self.theme["text"],
            wrap="word"
        )
        history_box.pack(fill="both", expand=True, padx=15, pady=10)

        records = load_history()

        if not records:
            history_box.insert("end", "No saved operations yet.")
        else:
            for record in history_generator(records):
                operation_id, expression, result, created_at = record
                history_box.insert(
                    "end",
                    f"{operation_id}. {expression} = {result} | {created_at}\n"
            )

        def clear_history():
            clear_all_history()
            history_box.delete("1.0", "end")
            history_box.insert("end", "History cleared successfully.")

        clear_button = tk.Button(
            history_window,
            text="Clear History",
            font=("Segoe UI", 12),
            bg="#d9534f",
            fg="white",
            command=clear_history
        )
        clear_button.pack(pady=10)
    