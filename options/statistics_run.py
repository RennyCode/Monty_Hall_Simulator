from tkinter import ttk
from tkinter import *

from algo_setup import game_run
from functions import create_new_window, play_sound, restart_program, load_image


def statistics(main_frame):
    # Create new frame for 'PC Multi-Run'
    pc_multirun_frame = create_new_window(main_frame)

    Label(pc_multirun_frame, text="Times to run:").grid(column=1, row=0, pady=10)

    times_to_run = ttk.Combobox(pc_multirun_frame, width=27, state="readonly")
    times_to_run["values"] = (
        100,
        500,
        1000,
        2500,
        5000,
        10000,
        25000,
        100000,
        500000,
        1000000,
    )
    times_to_run.set(100)
    times_to_run.grid(column=1, row=1)

    # Times to run select button
    Button(
        pc_multirun_frame,
        text="Select",
        command=lambda: pc_multirun_res(pc_multirun_frame, int(times_to_run.get())),
    ).grid(column=1, row=6, pady=10)
    mainloop()


def pc_multirun_res(pc_multirun_frame, n):
    # Create new frame for displaying the results
    pc_multirun_frame_res = create_new_window(pc_multirun_frame)

    # Run the Monty Hall algorithm -> returns Win (True) / Lose (False)
    text_box = Label(pc_multirun_frame_res, width=100, text="")
    text_box.grid(column=0, row=0)
    wins = game_run(n, False, text_box)

    # Play sound conditionally, depends on Win / Lose
    play_sound(
        "assets/sounds/ApplauseSound.wav" if wins else "assets/sounds/GoatSound.mp3"
    )

    goat_img = load_image("assets/images/goat_image.jpg", 200, 150)
    car_img = load_image("assets/images/car_image.jpg", 200, 150)

    # Render image conditionally, depends on Win / Lose
    Label(pc_multirun_frame_res, image=car_img if wins else goat_img).place(
        relx=0.5, rely=0.5, anchor=CENTER
    )

    # Render texts conditionally, depends on Win / Lose
    Label(pc_multirun_frame_res, text="You Won!" if wins else "You Lost!").place(
        relx=0.5, rely=0.2, anchor=CENTER
    )
    Label(pc_multirun_frame_res, text="Choice changed").place(
        relx=0.5, rely=0.25, anchor=CENTER
    )

    # Restart button
    Button(
        pc_multirun_frame_res,
        text="Restart",
        command=lambda: restart_program(pc_multirun_frame_res)
    ).place(relx=0.5, rely=0.7, anchor=CENTER)
    mainloop()
