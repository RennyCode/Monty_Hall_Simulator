from tkinter import ttk


def create_style():
    style = ttk.Style()

    # title label
    style.configure(
        "T.Label",
        background="midnight blue",
        foreground="white",
        font=("Arial", 14, "bold"),
    )

    # Subtitle label
    style.configure(
        "ST.Label",
        background="midnight blue",
        foreground="white",
        font=("Arial", 12, "bold"),
    )

    # Partition title label
    style.configure(
        "PT.Label",
        background="midnight blue",
        foreground="gray60",
        font=("Arial", 10, "bold"),
    )

    # Partition numbering label
    style.configure(
        "PN.Label",
        background="midnight blue",
        foreground="white",
        font=("Arial", 11, "bold"),
    )

    # Win / Lose label
    style.configure(
        "WL.Label",
        background="midnight blue",
        font=("Arial", 14, "bold"),
    )

    # Button
    style.configure(
        "TButton",
        padding=15,
        font=("Arial", 11, "bold"),
    )

    return style
