import tkinter as tk
from app.calculator import Calculator
from storage.database import create_table

def main():
    create_table()
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()


if __name__ == "__main__":
    main()