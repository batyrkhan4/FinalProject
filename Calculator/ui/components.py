import tkinter as tk


def create_header(app):
    if hasattr(app, "header"):
        app.header.destroy()

    app.header = tk.Frame(
        app.root,
        bg=app.theme["bg"]
    )

    app.header.pack(fill="x")

    tk.Button(
        app.header,
        text="☰",
        font=("Segoe UI", 18),
        bg=app.theme["bg"],
        fg=app.theme["text"],
        bd=0,
        command=app.open_menu
    ).pack(side="left", padx=10)

    app.title = tk.Label(
        app.header,
        text=app.mode.title(),
        font=("Segoe UI", 20, "bold"),
        bg=app.theme["bg"],
        fg=app.theme["text"]
    )

    app.title.pack(side="left")

    tk.Button(
        app.header,
        text="⚙",
        bg=app.theme["bg"],
        fg=app.theme["text"],
        bd=0,
        command=app.open_settings
    ).pack(side="right", padx=10)

    tk.Button(
        app.header,
        text="🕒",
        bg=app.theme["bg"],
        fg=app.theme["text"],
        bd=0,
        command=app.open_history
    ).pack(side="right")


def create_display(app):
    if hasattr(app, "display"):
        app.display.destroy()

    app.display = tk.Entry(
        app.root,
        font=("Segoe UI", 35),
        bg=app.theme["bg"],
        fg=app.theme["text"],
        bd=0,
        justify="right"
    )

    app.display.pack(
        fill="x",
        padx=20,
        pady=(20, 40),
        ipady=30
    )


def create_buttons(app):
    if hasattr(app, "frame"):
        app.frame.destroy()

    app.frame = tk.Frame(
        app.root,
        bg=app.theme["bg"]
    )

    app.frame.pack(
        expand=True,
        fill="both"
    )

    app.load_buttons()