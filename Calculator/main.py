import tkinter as tk
from app.calculator import Calculator

def main():
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()


if __name__ == "__main__":
    main()