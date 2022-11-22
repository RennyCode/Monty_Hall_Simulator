from tkinter import *
import pygame

# Import useful functions
from functions import create_new_window, load_image

# Import all game options
from options.manual_run import manual
from options.statistics_run import statistics
from options.pc_single_run import pc_single_run

# Initiate root
root = Tk()
root.title("Monty Hall Problem")
root.geometry("650x500")  # Window size
root.resizable(False, False)  # Setting the window to be un-resizable

# Combobox style configuration
root.option_add("*TCombobox*Listbox.font", ("Arial", "12"))
root.option_add("*TCombobox*Listbox.Justify", "center")

# Pygame sound mixer initiator
pygame.mixer.init()


# Function to load main (initial) screen
def main_screen(frame: Frame = None) -> None:
    main_frame = create_new_window(frame)

    # Title
    Label(
        main_frame,
        text="Welcome To The Monty Hall Game",
        bg="midnight blue",
        fg="white",
        font=("Arial", 14, "bold"),
    ).grid(column=0, row=0, columnspan=3, pady=30)

    curtains_img = load_image("assets/images/curtains_image.webp", 200, 150)

    # Render 3 curtain images to screen
    for i in range(3):
        Label(main_frame, image=curtains_img).grid(column=i, row=1)

    Label(
        main_frame,
        text="Choose Game Type:",
        bg="midnight blue",
        font=("Arial", 12, "bold"),
    ).grid(column=0, row=3, columnspan=3, pady=50)

    # PC Single-Run button
    Button(
        main_frame,
        text="PC One Game",
        height=3,
        width=15,
        font=("Arial", 11, "bold"),
        command=lambda: pc_single_run(main_frame),
    ).grid(column=0, row=4)
    # PC Multi-Run button
    Button(
        main_frame,
        text="Statistics",
        height=3,
        width=15,
        font=("Arial", 11, "bold"),
        command=lambda: statistics(main_frame),
    ).grid(column=1, row=4)
    # Human Run button
    Button(
        main_frame,
        text="Human Run",
        height=3,
        width=15,
        font=("Arial", 11, "bold"),
        command=lambda: manual(main_frame),
    ).grid(column=2, row=4)
    mainloop()


if __name__ == "__main__":
    main_screen()
