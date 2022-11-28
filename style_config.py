from tkinter import ttk

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