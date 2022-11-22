import random
from tkinter import *

from algo_setup import mh_problem_partial
from functions import create_new_window, load_image, restart_program, play_sound


def pc_single_run(main_frame: Frame) -> None:
    # Create new frame for 'PC Single Run'
    pc_single_frame = create_new_window(main_frame)

    # Randomize a choice
    choice = random.randint(0, 2)
    Label(
        pc_single_frame,
        text="\nPC chose curtain No." + str(choice + 1),
        bg="midnight blue",
        font=("Arial", 12, "bold"),
    ).grid(column=0, row=0, columnspan=3, pady=30)

    curtains_img = load_image("assets/images/curtains_image.webp", 200, 150)

    # Render 3 curtain images
    for i in range(3):
        Label(pc_single_frame, image=curtains_img).grid(column=i, row=1)

    # Next step button
    Button(
        pc_single_frame,
        text="Next Step",
        height=2,
        width=10,
        font=("Arial", 11, "bold"),
        command=lambda: pc_single_run_p2(pc_single_frame, choice),
    ).grid(column=1, row=2, pady=80)
    mainloop()


def pc_single_run_p2(pc_single_frame: Frame, choice: int) -> None:
    # Create new frame for next step
    pc_single_p2_frame = create_new_window(pc_single_frame)

    # Run the Monty Hall algorithm
    exposed_goat_index, obj_list = mh_problem_partial(choice)

    curtains_img = load_image("assets/images/curtains_image.webp", 200, 150)
    goat_img = load_image("assets/images/goat_image.jpg", 200, 150)

    text_box = Label(
        pc_single_p2_frame,
        text="\nThe PC's first choice was No."
        + str(choice + 1)
        + "\nThere is a goat behind curtain No."
        + str(exposed_goat_index + 1),
        bg="midnight blue",
        font=("Arial", 12, "bold"),
    )
    text_box.grid(column=0, row=0, columnspan=3, pady=30)
    Label(pc_single_p2_frame, image=goat_img).grid(column=exposed_goat_index, row=1)
    for i in range(3):
        if i != exposed_goat_index:
            Label(pc_single_p2_frame, image=curtains_img).grid(column=i, row=1)

    ci = obj_list.index("car")
    arr = [0, 1, 2]
    arr.remove(choice)
    arr.remove(exposed_goat_index)
    Button(
        pc_single_p2_frame,
        text="Next Step",
        height=2,
        width=10,
        font=("Arial", 11, "bold"),
        command=lambda: pc_single_run_res(pc_single_p2_frame, arr[0], ci),
    ).grid(column=1, row=2, pady=80)
    mainloop()


def pc_single_run_res(pc_single_p2_frame: Frame, new_choice: int, ci: int) -> None:
    pc_single_res_frame = create_new_window(pc_single_p2_frame)

    for i in range(4):
        pc_single_res_frame.grid_rowconfigure(i, weight=1)


    goat_img = load_image("assets/images/goat_image.jpg", 200, 150)
    car_img = load_image("assets/images/car_image.jpg", 200, 150)

    # Play sound conditionally, depends on Win / Lose
    if ci == new_choice:
        play_sound("assets/sounds/ApplauseSound.wav")
    else:
        play_sound("assets/sounds/GoatSound.mp3")

    Label(
        pc_single_res_frame,
        text="PC WON!" if ci == new_choice else "PC LOST!",
        bg="midnight blue",
        font=("Arial", 14, "bold"),
        fg="green" if ci == new_choice else "red",
    ).grid(column=0, row=0, columnspan=3, pady=(40, 0))
    Label(
        pc_single_res_frame,
        text="The PC changed its choice to curtain No." + str(new_choice + 1) + "!",
        bg="midnight blue",
        font=("Arial", 12, "bold"),
        fg="white",
    ).grid(column=0, row=1, columnspan=3)

    Label(pc_single_res_frame, image=car_img if ci == new_choice else goat_img).grid(
        column=0, row=2, columnspan=3
    )

    Button(
        pc_single_res_frame,
        text="Restart",
        height=2,
        width=10,
        font=("Arial", 11, "bold"),
        command=lambda: restart_program(pc_single_res_frame),
    ).grid(column=0, row=3, columnspan=3, pady=(0, 40))
    mainloop()
