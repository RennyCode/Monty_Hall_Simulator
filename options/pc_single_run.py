import random
from tkinter import *
from tkinter import ttk

from algo_setup import mh_problem_partial
from functions import create_new_window, load_image, restart_program, play_sound


def pc_single_run(main_frame: Frame) -> None:
    # Create new frame for 'PC Single Run'
    pc_single_frame = create_new_window(main_frame)

    # Randomize a choice
    choice = random.randint(0, 2)
    ttk.Label(
        pc_single_frame,
        text="\nPC chose partition No." + str(choice + 1),
        style="ST.Label"
    ).grid(column=0, row=0, columnspan=3, pady=20)

    curtains_img = load_image("assets/images/curtains_image.webp", 200, 150)

    # Render 3 curtain images
    for i in range(3):
        if choice == i:
            ttk.Label(
                pc_single_frame,
                text="⬇   Chosen   ⬇",
                style="PT.Label"
            ).grid(column=i, row=1, pady=20)
        Label(pc_single_frame, image=curtains_img).grid(column=i, row=2)
        Label(
            pc_single_frame,
            text="No." + str((i + 1)),
            bg="midnight blue",
            fg="white",
            font=("Arial", 11, "bold"),
        ).grid(column=i, row=3, pady=20)

    pc_single_frame.after(5000, lambda: pc_single_run_p2(pc_single_frame, choice))

    mainloop()


def pc_single_run_p2(pc_single_frame: Frame, choice: int) -> None:
    # Create new frame for next step
    pc_single_p2_frame = create_new_window(pc_single_frame)

    # Run the Monty Hall algorithm
    exposed_goat_index, obj_list = mh_problem_partial(choice)

    curtains_img = load_image("assets/images/curtains_image.webp", 200, 150)
    goat_img = load_image("assets/images/goat_image.jpg", 200, 150)

    ttk.Label(
        pc_single_p2_frame,
        text="PC Chose Partition: No." + str(choice + 1),
        style="ST.Label"
    ).grid(column=0, row=0, columnspan=3, pady=(30, 0))
    ttk.Label(
        pc_single_p2_frame,
        text="Exposed Goat Behind Partition: No." + str(exposed_goat_index + 1),
        style="ST.Label"
    ).grid(column=0, row=1, columnspan=3, pady=(10, 0))

    for i in range(3):
        if i == exposed_goat_index:
            ttk.Label(
                pc_single_p2_frame,
                text="▶   Exposed Goat   ◀",
                style="PT.Label"
            ).grid(column=i, row=2, pady=20)
            Label(pc_single_p2_frame, image=goat_img).grid(column=i, row=3)
        else:
            if i == choice:
                ttk.Label(
                    pc_single_p2_frame,
                    text="⬇   Chosen   ⬇",
                    style="PT.Label"
                ).grid(column=i, row=2, pady=20)
            Label(pc_single_p2_frame, image=curtains_img).grid(column=i, row=3)
        Label(
            pc_single_p2_frame,
            text="No." + str((i + 1)),
            bg="midnight blue",
            fg="white",
            font=("Arial", 11, "bold"),
        ).grid(column=i, row=4, pady=20)

    pc_single_frame.after(
        5000,
        lambda: pc_single_run_res(
            pc_single_p2_frame, obj_list, choice, exposed_goat_index
        ),
    )

    mainloop()


def get_new_choice(choice: int, exposed_goat_index: int) -> int:
    arr = [0, 1, 2]
    arr.remove(choice)
    arr.remove(exposed_goat_index)
    return arr[0]


def pc_single_run_res(
    pc_single_p2_frame: Frame, obj_list: list[str], choice: int, exposed_goat_index: int
) -> None:
    pc_single_res_frame = create_new_window(pc_single_p2_frame)

    new_choice = get_new_choice(choice, exposed_goat_index)

    goat_img = load_image("assets/images/goat_image.jpg", 200, 150)
    car_img = load_image("assets/images/car_image.jpg", 200, 150)

    # Play sound conditionally, depends on Win / Lose
    if obj_list.index("car") == new_choice:
        play_sound("assets/sounds/ApplauseSound.mp3")
    else:
        play_sound("assets/sounds/GoatSound.mp3")

    Label(
        pc_single_res_frame,
        text="PC WON!" if obj_list.index("car") == new_choice else "PC LOST!",
        bg="midnight blue",
        font=("Arial", 14, "bold"),
        fg="green" if obj_list.index("car") == new_choice else "red",
    ).grid(column=0, row=0, columnspan=3, pady=(30, 0))
    ttk.Label(
        pc_single_res_frame,
        text="The PC Changed its Choice to Partition No." + str(new_choice + 1) + "!",
        style="ST.Label"
    ).grid(column=0, row=1, columnspan=3, pady=(10, 0))

    for i, obj in enumerate(obj_list):
        if i == exposed_goat_index:
            ttk.Label(
                pc_single_res_frame,
                text="▶   Goat   ◀",
                style="PT.Label"
            ).grid(column=i, row=2, pady=20)
        elif i == choice:
            ttk.Label(
                pc_single_res_frame,
                text="⬇   First Choice   ⬇",
                style="PT.Label"
            ).grid(column=i, row=2, pady=20)
        else:
            ttk.Label(
                pc_single_res_frame,
                text="⬇   Second Choice   ⬇",
                style="PT.Label"
            ).grid(column=i, row=2, pady=20)
        Label(pc_single_res_frame, image=car_img if obj == "car" else goat_img).grid(
            column=i, row=3
        )
        Label(
            pc_single_res_frame,
            text="No." + str((i + 1)),
            bg="midnight blue",
            fg="white",
            font=("Arial", 11, "bold"),
        ).grid(column=i, row=4, pady=20)

    Button(
        pc_single_res_frame,
        text="Restart",
        height=2,
        width=10,
        font=("Arial", 11, "bold"),
        command=lambda: restart_program(pc_single_res_frame),
    ).grid(column=0, row=5, columnspan=3, pady=20)
    mainloop()
