from tkinter import *

from algo_setup import mh_problem_partial
from functions import create_new_window, play_sound, load_image, restart_program


def manual(main_frame: Frame) -> None:
    # Create new frame for 'Human Run'
    first_human_frame = create_new_window(main_frame)

    Label(
        first_human_frame,
        text="Choose a Partition:",
        bg="midnight blue",
        fg="white",
        font=("Arial", 12, "bold"),
    ).grid(column=0, row=0, columnspan=3, pady=30)

    # Load relevant images
    curtains_img = load_image("assets/images/curtains_image.webp", 200, 150)

    # Render 3 curtain images & 3 buttons to choose from
    for i in range(3):
        Label(first_human_frame, image=curtains_img).grid(column=i, row=1)
        if i == 0:
            Button(
                first_human_frame,
                text="No." + str(i + 1),
                height=2,
                width=10,
                font=("Arial", 11, "bold"),
                command=lambda: human_sec_choice(first_human_frame, 0),
            ).grid(column=i, row=2, pady=80)
        elif i == 1:
            Button(
                first_human_frame,
                text="No." + str(i + 1),
                height=2,
                width=10,
                font=("Arial", 11, "bold"),
                command=lambda: human_sec_choice(first_human_frame, 1),
            ).grid(column=i, row=2, pady=80)
        else:
            Button(
                first_human_frame,
                text="No." + str(i + 1),
                height=2,
                width=10,
                font=("Arial", 11, "bold"),
                command=lambda: human_sec_choice(first_human_frame, 2),
            ).grid(column=i, row=2, pady=80)
    mainloop()


def human_sec_choice(first_frame: Frame, first_choice: int) -> None:
    # Create new frame for screen after 1st choice
    second_human_frame = create_new_window(first_frame)

    # Run the Monty Hall algorithm -> return the exposed goat index & list
    exposed_goat_index, obj_list = mh_problem_partial(first_choice)

    Label(
        second_human_frame,
        text="Would You Like to Change Your Choice?",
        bg="midnight blue",
        fg="white",
        font=("Arial", 12, "bold"),
    ).grid(column=0, row=0, columnspan=3, pady=(30, 0))

    # Load relevant images
    curtains_img = load_image("assets/images/curtains_image.webp", 200, 150)
    goat_img = load_image("assets/images/goat_image.jpg", 200, 150)

    for i in range(3):
        if i == exposed_goat_index:
            Label(
                second_human_frame,
                text="▶   Exposed Goat   ◀",
                bg="midnight blue",
                fg="gray60",
                font=("Arial", 10, "bold"),
            ).grid(column=i, row=1, pady=20)
            Label(second_human_frame, image=goat_img).grid(column=i, row=2)
        else:
            if i == first_choice:
                Label(
                    second_human_frame,
                    text="⬇   Chosen   ⬇",
                    bg="midnight blue",
                    fg="gray60",
                    font=("Arial", 10, "bold"),
                ).grid(column=i, row=1, pady=20)
            Label(second_human_frame, image=curtains_img).grid(column=i, row=2)
            if i == 0:
                Button(
                    second_human_frame,
                    text="Change" if i != first_choice else "Don't\nChange",
                    height=2,
                    width=10,
                    font=("Arial", 11, "bold"),
                    command=lambda: human_results(
                        second_human_frame, first_choice, 0, obj_list
                    ),
                ).grid(column=i, row=4, pady=30)
            elif i == 1:
                Button(
                    second_human_frame,
                    text="Change" if i != first_choice else "Don't\nChange",
                    height=2,
                    width=10,
                    font=("Arial", 11, "bold"),
                    command=lambda: human_results(
                        second_human_frame, first_choice, 1, obj_list
                    ),
                ).grid(column=i, row=4, pady=30)
            else:
                Button(
                    second_human_frame,
                    text="Change" if i != first_choice else "Don't\nChange",
                    height=2,
                    width=10,
                    font=("Arial", 11, "bold"),
                    command=lambda: human_results(
                        second_human_frame, first_choice, 2, obj_list
                    ),
                ).grid(column=i, row=4, pady=30)
        Label(
            second_human_frame,
            text="No." + str((i + 1)),
            bg="midnight blue",
            fg="white",
            font=("Arial", 11, "bold"),
        ).grid(column=i, row=3, pady=20)
    mainloop()


def human_results(
    second_human_frame: Frame,
    first_choice: int,
    second_choice: int,
    obj_list: list[str],
) -> None:
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
    Label(
        human_results_frame,
        text="YOU WON!" if ci == second_choice else "YOU LOST!",
        bg="midnight blue",
        font=("Arial", 14, "bold"),
        fg="green" if ci == second_choice else "red",
    ).grid(column=0, row=0, columnspan=3, pady=(30, 0))
    Label(
        human_results_frame,
        text="You Changed Your Choice!"
        if first_choice != second_choice
        else "You Didn't Change Your Choice!",
        bg="midnight blue",
        font=("Arial", 12, "bold"),
        fg="white",
    ).grid(column=0, row=1, columnspan=3, pady=(10, 0))

    # Load relevant images
    goat_img = load_image("assets/images/goat_image.jpg", 200, 150)
    car_img = load_image("assets/images/car_image.jpg", 200, 150)

    # Render image conditionally, depends on Win / Lose
    # Label(human_results_frame, image=car_img if ci == second_choice else goat_img).grid(
    #     column=0, row=2, columnspan=3
    # )

    for i, obj in enumerate(obj_list):
        if i == first_choice:
            Label(
                human_results_frame,
                text="⬇   Your Choice   ⬇" if first_choice == second_choice else "⬇   First Choice   ⬇",
                bg="midnight blue",
                fg="gray60",
                font=("Arial", 10, "bold"),
            ).grid(column=i, row=2, pady=20)
        elif i == second_choice:
            Label(
                human_results_frame,
                text="⬇   Your Choice   ⬇" if first_choice == second_choice else "⬇   Second Choice   ⬇",
                bg="midnight blue",
                fg="gray60",
                font=("Arial", 10, "bold"),
            ).grid(column=i, row=2, pady=20)
        else:
            Label(
                human_results_frame,
                text="▶   Goat   ◀" if obj == "goat" else "▶   Car   ◀",
                bg="midnight blue",
                fg="gray60",
                font=("Arial", 10, "bold"),
            ).grid(column=i, row=2, pady=20)
        Label(human_results_frame, image=car_img if obj == "car" else goat_img).grid(
            column=i, row=3
        )
        Label(
            human_results_frame,
            text="No." + str((i + 1)),
            bg="midnight blue",
            fg="white",
            font=("Arial", 11, "bold"),
        ).grid(column=i, row=4, pady=20)

    # Restart button
    Button(
        human_results_frame,
        text="Restart",
        height=2,
        width=10,
        font=("Arial", 11, "bold"),
        command=lambda: restart_program(human_results_frame),
    ).grid(column=0, row=5, columnspan=3, pady=20)
    mainloop()
