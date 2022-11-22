from tkinter import *

from algo_setup import mh_problem_partial
from functions import create_new_window, play_sound, load_image, restart_program


def human_run(main_frame):
    # Create new frame for 'Human Run'
    first_human_frame = create_new_window(main_frame)

    Label(first_human_frame, text="Make your choice").grid(column=1, row=0, pady=10)

    # Load relevant images
    curtains_img = load_image("assets/images/curtains_image.webp", 200, 150)

    # Render 3 curtain images & 3 buttons to choose from
    for i in range(3):
        Label(first_human_frame, image=curtains_img).grid(column=i, row=1)
        if i == 0:
            Button(
                first_human_frame,
                text="No." + str(i + 1),
                command=lambda: human_sec_choice(0, first_human_frame),
            ).grid(column=i, row=2, pady=10)
        elif i == 1:
            Button(
                first_human_frame,
                text="No." + str(i + 1),
                command=lambda: human_sec_choice(1, first_human_frame),
            ).grid(column=i, row=2, pady=10)
        else:
            Button(
                first_human_frame,
                text="No." + str(i + 1),
                command=lambda: human_sec_choice(2, first_human_frame),
            ).grid(column=i, row=2, pady=10)
    mainloop()


def human_sec_choice(first_choice, first_frame):
    # Create new frame for screen after 1st choice
    print("first:" + str(first_choice))
    second_human_frame = create_new_window(first_frame)

    # Run the Monty Hall algorithm -> return the exposed goat index & list
    exposed_goat_index, obj_list = mh_problem_partial(first_choice)
    print("exposed:" + str(exposed_goat_index))

    Label(second_human_frame, text="Would you like to change your choice?").grid(
        column=1, row=0, pady=10
    )

    # Load relevant images
    curtains_img = load_image("assets/images/curtains_image.webp", 200, 150)
    goat_img = load_image("assets/images/goat_image.jpg", 200, 150)

    for i in range(3):
        if i == exposed_goat_index:
            image_label = Label(second_human_frame, image=goat_img)
        else:
            image_label = Label(second_human_frame, image=curtains_img)
            if i == 0:
                Button(
                    second_human_frame,
                    text="Change" if i != first_choice else "Stand",
                    command=lambda: human_results(
                        first_choice, 0, obj_list, second_human_frame
                    ),
                ).grid(column=i, row=2)
            elif i == 1:
                Button(
                    second_human_frame,
                    text="Change" if i != first_choice else "Stand",
                    command=lambda: human_results(
                        first_choice, 1, obj_list, second_human_frame
                    ),
                ).grid(column=i, row=2)
            else:
                Button(
                    second_human_frame,
                    text="Change" if i != first_choice else "Stand",
                    command=lambda: human_results(
                        first_choice, 2, obj_list, second_human_frame
                    ),
                ).grid(column=i, row=2)
        image_label.grid(column=i, row=1)
    mainloop()


def human_results(first_choice, second_choice, obj_list, second_human_frame):
    # Create new frame for displaying the results
    human_results_frame = create_new_window(second_human_frame)

    ci = obj_list.index("car")

    # Render texts conditionally, depends on Win / Lose
    Label(
        human_results_frame, text="You Won!" if ci == second_choice else "You Lost!"
    ).place(relx=0.5, rely=0.2, anchor=CENTER)
    Label(
        human_results_frame,
        text="Choice changed"
        if first_choice != second_choice
        else "Choice not changed",
    ).place(relx=0.5, rely=0.25, anchor=CENTER)

    # Load relevant images
    goat_img = load_image("assets/images/goat_image.jpg", 200, 150)
    car_img = load_image("assets/images/car_image.jpg", 200, 150)

    # Render image conditionally, depends on Win / Lose
    image_label = Label(
        human_results_frame, image=car_img if ci == second_choice else goat_img
    )
    image_label.place(relx=0.5, rely=0.5, anchor=CENTER)

    # Play sound conditionally, depends on Win / Lose
    if ci == second_choice:
        play_sound("assets/sounds/ApplauseSound.wav")
    else:
        play_sound("assets/sounds/GoatSound.mp3")

    # Restart button
    Button(
        human_results_frame,
        text="Restart",
        command=lambda: restart_program(human_results_frame),
    ).place(relx=0.5, rely=0.7, anchor=CENTER)
    mainloop()
