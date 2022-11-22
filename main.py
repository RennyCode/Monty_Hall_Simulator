from tkinter import *
import pygame

# Import useful functions
from functions import create_new_window, load_image

# import all game options
from options.manual_run import human_run
from options.statistics_run import statistics
from options.pc_single_run import pc_single_run

# Initiate root
root = Tk()
root.title("Monty Hall Problem")
root.geometry("650x500")
root.resizable(False, False)
pygame.mixer.init()

# Load curtain image
curtains_img = load_image("assets/images/curtains_image.webp", 200, 150)


# Function to load main (initial) screen
def main_screen(frame=None):
    main_frame = create_new_window(frame)

    # Title
    Label(main_frame, text="Welcome To The Monty Hall Game", bg='orange red', fg='white', font=("Arial", 10, 'bold')).grid(
        column=1, row=0, pady=10
    )

    # Render 3 curtain images to screen
    for i in range(3):
        Label(main_frame, image=curtains_img).grid(column=i, row=1)

    Label(main_frame, text="Choose Game Type:", bg='orange red').grid(column=1, row=3, pady=10)

    # PC Single-Run button
    Button(
        main_frame, text="PC One Game", command=lambda: pc_single_run(main_frame)
    ).grid(column=0, row=4, pady=10)
    # PC Multi-Run button
    Button(main_frame, text="Statistics", command=lambda: statistics(main_frame)).grid(
        column=1, row=4, pady=10
    )
    # Human Run button
    Button(main_frame, text="Human Run", command=lambda: human_run(main_frame)).grid(
        column=2, row=4, pady=10
    )
    mainloop()


if __name__ == "__main__":
    main_screen()
