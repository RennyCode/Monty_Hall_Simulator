from tkinter import *
from tkinter import ttk

# Import utils
from utils.algo_setup import mh_problem_partial
from utils.functions import (
    create_new_window,
    play_sound,
    load_image,
    render_restart_button,
)


def manual(main_frame: Frame) -> None:
    """Creates first manual-run window with partitions and selection buttons

    :param main_frame: Previous frame to destroy
    :type main_frame: Frame
    :return: None
    """

    # Create new frame of 'Human Run'
    first_human_frame = create_new_window(main_frame)

    # Instruction label for 1st manual-run
    ttk.Label(first_human_frame, text="Choose a Partition:", style="ST.Label").grid(
        column=0, row=0, columnspan=3, pady=30
    )

    # Load curtains image to variable
    curtains_img = load_image("assets/images/curtains_image.webp", 200, 150)

    # Render 3 curtain images & 3 buttons to choose from
    for i in range(3):
        Label(first_human_frame, image=curtains_img).grid(column=i, row=1)
        if i == 0:
            ttk.Button(
                first_human_frame,
                text="No." + str(i + 1),
                style="TButton",
                command=lambda: human_sec_choice(first_human_frame, 0),
            ).grid(column=i, row=2, pady=80)
        elif i == 1:
            ttk.Button(
                first_human_frame,
                text="No." + str(i + 1),
                style="TButton",
                command=lambda: human_sec_choice(first_human_frame, 1),
            ).grid(column=i, row=2, pady=80)
        else:
            ttk.Button(
                first_human_frame,
                text="No." + str(i + 1),
                style="TButton",
                command=lambda: human_sec_choice(first_human_frame, 2),
            ).grid(column=i, row=2, pady=80)

    mainloop()


def human_sec_choice(first_frame: Frame, first_choice: int) -> None:
    """Creates second manual-run window similar to previous one,
    only with different buttons (according to previous frame)

    :param first_frame: Previous frame to destroy
    :type first_frame: Frame
    :param first_choice: Index of first choice
    :type first_choice: int
    :return: None
    """

    # Create new frame for screen after 1st choice
    second_human_frame = create_new_window(first_frame)

    # Run the Monty Hall algorithm -> return the exposed goat index & list
    exposed_goat_index, obj_list = mh_problem_partial(first_choice)

    # Instructions label for 2nd manual-run
    ttk.Label(
        second_human_frame,
        text="Would You Like to Change Your Choice?",
        style="ST.Label",
    ).grid(column=0, row=0, columnspan=3, pady=(30, 0))

    # Load curtains and goat images to variables
    curtains_img = load_image("assets/images/curtains_image.webp", 200, 150)
    goat_img = load_image("assets/images/goat_image.jpg", 200, 150)

    # Render curtains and goat images relying on the algorithm return values and user's choice
    # Also, render captions and buttons accordingly
    for i in range(3):
        if i == exposed_goat_index:
            ttk.Label(
                second_human_frame, text="▶   Exposed Goat   ◀", style="PT.Label"
            ).grid(column=i, row=1, pady=20)
            Label(second_human_frame, image=goat_img).grid(column=i, row=2)
        else:
            if i == first_choice:
                ttk.Label(
                    second_human_frame, text="⬇   Chosen   ⬇", style="PT.Label"
                ).grid(column=i, row=1, pady=20)
            Label(second_human_frame, image=curtains_img).grid(column=i, row=2)
            if i == 0:
                ttk.Button(
                    second_human_frame,
                    text="Change" if i != first_choice else "Don't Change",
                    style="TButton",
                    command=lambda: human_results(
                        second_human_frame, first_choice, 0, obj_list
                    ),
                ).grid(column=i, row=4, pady=30)
            elif i == 1:
                ttk.Button(
                    second_human_frame,
                    text="Change" if i != first_choice else "Don't Change",
                    style="TButton",
                    command=lambda: human_results(
                        second_human_frame, first_choice, 1, obj_list
                    ),
                ).grid(column=i, row=4, pady=30)
            else:
                ttk.Button(
                    second_human_frame,
                    text="Change" if i != first_choice else "Don't Change",
                    style="TButton",
                    command=lambda: human_results(
                        second_human_frame, first_choice, 2, obj_list
                    ),
                ).grid(column=i, row=4, pady=30)
        ttk.Label(second_human_frame, text="No." + str((i + 1)), style="PN.Label").grid(
            column=i, row=3, pady=20
        )
    mainloop()


def human_results(
    second_human_frame: Frame,
    first_choice: int,
    second_choice: int,
    obj_list: list[str],
) -> None:
    """Creates third (and final) manual-run window, presenting results of the user's choice
    (i.e. win / lose condition) and exposure of the objects behind the partitions

    :param second_human_frame: Previous frame to destroy
    :type second_human_frame: Frame
    :param first_choice: Index of user's first choice
    :type first_choice: int
    :param second_choice: Index of user's second choice
    :type second_choice: int
    :param obj_list: list of objects order behind partitions (i.e. goats and car)
    :type obj_list: list[str]
    :return: None
    """

    # Create new frame for displaying the results
    human_results_frame = create_new_window(second_human_frame)

    # Get index of car in list
    ci = obj_list.index("car")

    # Play sound conditionally, depends on Win / Lose
    if ci == second_choice:
        play_sound("assets/sounds/ApplauseSound.mp3")
    else:
        play_sound("assets/sounds/GoatSound.mp3")

    # Render texts conditionally, depends on Win / Lose
    ttk.Label(
        human_results_frame,
        text="YOU WON!" if ci == second_choice else "YOU LOST!",
        style="WL.Label",
        foreground="green" if ci == second_choice else "red",
    ).grid(column=0, row=0, columnspan=3, pady=(30, 0))
    ttk.Label(
        human_results_frame,
        text="You Changed Your Choice!"
        if first_choice != second_choice
        else "You Didn't Change Your Choice!",
        style="ST.Label",
    ).grid(column=0, row=1, columnspan=3, pady=(10, 0))

    # Load goat and car images to variables
    goat_img = load_image("assets/images/goat_image.jpg", 200, 150)
    car_img = load_image("assets/images/car_image.jpg", 200, 150)

    # Render objects images as returned from algorithm
    # Also, render captions according to algorithm return values and the user's choice
    for i, obj in enumerate(obj_list):
        if i == first_choice:
            ttk.Label(
                human_results_frame,
                text="⬇   Your Choice   ⬇"
                if first_choice == second_choice
                else "⬇   First Choice   ⬇",
                style="PT.Label",
            ).grid(column=i, row=2, pady=20)
        elif i == second_choice:
            ttk.Label(
                human_results_frame,
                text="⬇   Your Choice   ⬇"
                if first_choice == second_choice
                else "⬇   Second Choice   ⬇",
                style="PT.Label",
            ).grid(column=i, row=2, pady=20)
        else:
            ttk.Label(
                human_results_frame,
                text="▶   Goat   ◀" if obj == "goat" else "▶   Car   ◀",
                style="PT.Label",
            ).grid(column=i, row=2, pady=20)
        Label(human_results_frame, image=car_img if obj == "car" else goat_img).grid(
            column=i, row=3
        )
        ttk.Label(
            human_results_frame, text="No." + str((i + 1)), style="PN.Label"
        ).grid(column=i, row=4, pady=20)

    # Restart button
    render_restart_button(human_results_frame, 5, 3)

    mainloop()
