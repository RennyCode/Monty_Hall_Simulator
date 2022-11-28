import random
from tkinter import *
from tkinter import ttk

# Import utils
from utils.algo_setup import mh_problem_partial
from utils.functions import (
    create_new_window,
    load_image,
    play_sound,
    render_restart_button,
)


def pc_single_run(main_frame: Frame) -> None:
    """Creates first PC-single-run window with partitions

    :param main_frame: Previous frame to destroy
    :type main_frame: Frame
    :return: None
    """

    # Create new frame for 'PC Single Run'
    pc_single_frame = create_new_window(main_frame)

    # Randomize a choice
    choice = random.randint(0, 2)
    ttk.Label(
        pc_single_frame,
        text="PC Chose Partition: No." + str(choice + 1),
        style="ST.Label",
    ).grid(column=0, row=0, columnspan=3, pady=20)

    # Load curtains image to variable
    curtains_img = load_image("assets/images/curtains_image.webp", 200, 150)

    # Render 3 partition images with captions according to PC's choice
    for i in range(3):
        if choice == i:
            ttk.Label(pc_single_frame, text="⬇   Chosen   ⬇", style="PT.Label").grid(
                column=i, row=1, pady=20
            )
        Label(pc_single_frame, image=curtains_img).grid(column=i, row=2)
        ttk.Label(pc_single_frame, text="No." + str((i + 1)), style="PN.Label").grid(
            column=i, row=3, pady=20
        )

    # 5 seconds delay before moving to next frame
    pc_single_frame.after(5000, lambda: pc_single_run_p2(pc_single_frame, choice))

    mainloop()


def pc_single_run_p2(pc_single_frame: Frame, choice: int) -> None:
    """Creates second PC-single-run window similar to previous one,
    only with more captions and details

    :param pc_single_frame: Previous frame to destroy
    :type pc_single_frame: Frame
    :param choice: Index of first choice
    :type choice: int
    :return: None
    """

    # Create new frame for screen after 1st choice
    pc_single_p2_frame = create_new_window(pc_single_frame)

    # Run the Monty Hall algorithm
    exposed_goat_index, obj_list = mh_problem_partial(choice)

    # Load curtains and goat images to variables
    curtains_img = load_image("assets/images/curtains_image.webp", 200, 150)
    goat_img = load_image("assets/images/goat_image.jpg", 200, 150)

    # Render description of PC's choice and exposed goat location
    ttk.Label(
        pc_single_p2_frame,
        text="PC Chose Partition: No." + str(choice + 1),
        style="ST.Label",
    ).grid(column=0, row=0, columnspan=3, pady=(30, 0))
    ttk.Label(
        pc_single_p2_frame,
        text="Exposed Goat Behind Partition: No." + str(exposed_goat_index + 1),
        style="ST.Label",
    ).grid(column=0, row=1, columnspan=3, pady=(10, 0))

    # Render curtains and goat images relying on the algorithm return values and PC's choice
    # Also, render captions accordingly
    for i in range(3):
        if i == exposed_goat_index:
            ttk.Label(
                pc_single_p2_frame, text="▶   Exposed Goat   ◀", style="PT.Label"
            ).grid(column=i, row=2, pady=20)
            Label(pc_single_p2_frame, image=goat_img).grid(column=i, row=3)
        else:
            if i == choice:
                ttk.Label(
                    pc_single_p2_frame, text="⬇   Chosen   ⬇", style="PT.Label"
                ).grid(column=i, row=2, pady=20)
            Label(pc_single_p2_frame, image=curtains_img).grid(column=i, row=3)
        ttk.Label(pc_single_p2_frame, text="No." + str((i + 1)), style="PN.Label").grid(
            column=i, row=4, pady=20
        )

    # 5 seconds delay before moving to next frame
    pc_single_frame.after(
        5000,
        lambda: pc_single_run_res(
            pc_single_p2_frame, obj_list, choice, exposed_goat_index
        ),
    )

    mainloop()


def get_new_choice(choice: int, exposed_goat_index: int) -> int:
    """Gets index of choice in list and exposed in order to determine the new choice

    :param choice: Index of first choice
    :type choice: int
    :param exposed_goat_index: Index of exposed goat index
    :type exposed_goat_index: int
    :return: Index of new choice
    :rtype: int
    """

    arr = [0, 1, 2]
    arr.remove(choice)
    arr.remove(exposed_goat_index)
    return arr[0]


def pc_single_run_res(
    pc_single_p2_frame: Frame, obj_list: list[str], choice: int, exposed_goat_index: int
) -> None:
    """Creates third (and final) PC-single-run window, presenting results of the PC's choice
    (i.e. win / lose condition) and exposure of the objects behind the partitions

    :param pc_single_p2_frame: Previous frame to destroy
    :type pc_single_p2_frame: Frame
    :param obj_list: list of objects order behind partitions (i.e. goats and car)
    :type obj_list: list[str]
    :param choice: Index of first choice
    :type choice: int
    :param exposed_goat_index: Index of exposed goat index
    :type exposed_goat_index: int
    :return: None
    """

    # Create new frame for displaying the results
    pc_single_res_frame = create_new_window(pc_single_p2_frame)

    # Get new choice of computer
    new_choice = get_new_choice(choice, exposed_goat_index)

    # Play sound conditionally, depends on Win / Lose
    if obj_list.index("car") == new_choice:
        play_sound("assets/sounds/ApplauseSound.mp3")
    else:
        play_sound("assets/sounds/GoatSound.mp3")

    # Render texts conditionally, depends on Win / Lose
    ttk.Label(
        pc_single_res_frame,
        text="PC WON!" if obj_list.index("car") == new_choice else "PC LOST!",
        style="WL.Label",
        foreground="green" if obj_list.index("car") == new_choice else "red",
    ).grid(column=0, row=0, columnspan=3, pady=(30, 0))
    ttk.Label(
        pc_single_res_frame,
        text="The PC Changed its Choice to Partition No." + str(new_choice + 1) + "!",
        style="ST.Label",
    ).grid(column=0, row=1, columnspan=3, pady=(10, 0))

    # Load goat and car images to variables
    goat_img = load_image("assets/images/goat_image.jpg", 200, 150)
    car_img = load_image("assets/images/car_image.jpg", 200, 150)

    # Render objects images as returned from algorithm
    # Also, render captions according to algorithm return values and the PC's choice
    for i, obj in enumerate(obj_list):
        if i == exposed_goat_index:
            ttk.Label(pc_single_res_frame, text="▶   Goat   ◀", style="PT.Label").grid(
                column=i, row=2, pady=20
            )
        elif i == choice:
            ttk.Label(
                pc_single_res_frame, text="⬇   First Choice   ⬇", style="PT.Label"
            ).grid(column=i, row=2, pady=20)
        else:
            ttk.Label(
                pc_single_res_frame, text="⬇   Second Choice   ⬇", style="PT.Label"
            ).grid(column=i, row=2, pady=20)
        Label(pc_single_res_frame, image=car_img if obj == "car" else goat_img).grid(
            column=i, row=3
        )
        ttk.Label(
            pc_single_res_frame, text="No." + str((i + 1)), style="PN.Label"
        ).grid(column=i, row=4, pady=20)

    # Restart Button
    render_restart_button(pc_single_res_frame, 5, 3)

    mainloop()
