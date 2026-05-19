import tkinter as tk

from math import pi, e, log
from core.functions import *
from storage.history import *

def handle_click(app, value):
    current = app.display.get()
    try:
        if value == "2ⁿᵈ":
            app.second_mode = not app.second_mode
            for x in app.frame.winfo_children():
                x.destroy()
            app.load_buttons()
            return
        if value in ["C","CE"]:
            app.display.delete(
                0,
                tk.END
            )
            return
        if value == "⌫":
            if current:
                app.display.delete(
                    len(current)-1,
                    tk.END
                )
            return
        if value == "+/-":
            if current and current != "Error":
                num = -float(current)
                app.display.delete(
                    0,
                    tk.END
                )
                app.display.insert(
                    0,
                    num
                )
            return


        if value == "π":

            app.display.insert(
                tk.END,
                str(pi)
            )

            return

        if value == "e":

            app.display.insert(
                tk.END,
                str(e)
            )

            return


        # ---------- LOG BASE ----------

        if value == "logᵧx":

            if current:

                app.saved_value = float(current)

                app.waiting_log = True

                app.display.delete(
                    0,
                    tk.END
                )

            return


        # ---------- POWER ----------

        if value == "xʸ":

            app.display.insert(
                tk.END,
                "**"
            )

            return


        # ---------- EQUAL ----------

        if value == "=":

            if app.waiting_log:

                base = float(current)

                result = str(
                    log(
                        app.saved_value,
                        base
                    )
                )

                app.waiting_log = False

            else:

                result = str(

                    eval(
                        current
                        .replace("×","*")
                        .replace("÷","/")
                    )

                )

            app.display.delete(
                0,
                tk.END
            )

            app.display.insert(
                0,
                result
            )

            return


        # ---------- FUNCTIONS ----------

        if value == "x²":
            result = square(float(current))

        elif value == "x³":
            result = cube(float(current))

        elif value == "1/x":
            result = inverse(float(current))

        elif value in ["√","²√x"]:
            result = square_root(float(current))

        elif value == "³√x":
            result = cube_root(float(current))

        elif value == "|x|":
            result = absolute(float(current))

        elif value == "sin":
            result = sine(float(current))

        elif value == "cos":
            result = cosine(float(current))

        elif value == "tan":
            result = tangent(float(current))

        elif value == "cot":
            result = cotangent(float(current))

        elif value == "10ˣ":
            result = ten_power(float(current))

        elif value == "2ˣ":
            result = two_power(float(current))

        elif value == "eˣ":
            result = exponent(float(current))

        elif value == "log":
            result = common_log(float(current))

        elif value == "ln":
            result = natural_log(float(current))

        elif value == "n!":
            result = factorial_num(float(current))

        else:

            # обычные цифры и символы

            app.display.insert(
                tk.END,
                value
            )

            return


        app.display.delete(
            0,
            tk.END
        )

        app.display.insert(
            0,
            result
        )


    except:

        app.display.delete(
            0,
            tk.END
        )

        app.display.insert(
            0,
            "Error"
        )