import random
from tkinter import *

from algo_setup import mh_problem_partial
from functions import create_new_window, load_image, restart_program, play_sound


def pc_single_run(main_frame):
    # Create new frame for 'PC Single Run'
    pc_single_frame = create_new_window(main_frame)

    # Randomize a choice
    choice = random.randint(0, 2)
    Label(pc_single_frame, text="\nThe PC choice was No." + str(choice + 1)).grid(
        column=1, row=0, pady=10
    )

    curtains_img = load_image("assets/images/curtains_image.webp", 200, 150)

    # Render 3 curtain images
    for i in range(3):
        Label(pc_single_frame, image=curtains_img).grid(column=i, row=1)

    # Next step button
    Button(
        pc_single_frame,
        text="Next Step",
        command=lambda: pc_single_run_p2(pc_single_frame, choice),
    ).grid(column=1, row=2, pady=10)
    mainloop()


def pc_single_run_p2(pc_single_frame, choice):
    # Create new frame for next step
    pc_single_p2_frame = create_new_window(pc_single_frame)

    # Run the Monty Hall algorithm -> return the exposed goat index & list
    exposed_goat_index, obj_list = mh_problem_partial(choice)
    curtains_img = load_image("assets/images/curtains_image.webp", 200, 150)
    goat_img = load_image("assets/images/goat_image.jpg", 200, 150)
    text_box = Label(
        pc_single_p2_frame,
        text="\nThe PC first choice was No."
        + str(choice + 1)
        + "\nThe game show expose curtain NO."
        + str(exposed_goat_index + 1),
    )
    text_box.grid(column=1, row=0, pady=10)
    Label(pc_single_p2_frame, image=goat_img).grid(column=exposed_goat_index, row=1)
    for i in range(3):
        if i != exposed_goat_index:
            Label(pc_single_p2_frame, image=curtains_img).grid(column=i, row=1)

    print("old choice: " + str(choice))
    print("expose goat: " + str(exposed_goat_index))
    ci = obj_list.index("car")
    arr = [0, 1, 2]
    arr.remove(choice)
    arr.remove(exposed_goat_index)
    print("new choice: " + str(arr[0]))
    Button(
        pc_single_p2_frame,
        text="Next Step",
        command=lambda: pc_single_run_res(pc_single_p2_frame, arr[0], ci),
    ).grid(column=1, row=2, pady=10)
    mainloop()


def pc_single_run_res(pc_single_p2_frame, new_choice, ci):
    pc_single_res_frame = create_new_window(pc_single_p2_frame)

    text_box = Label(
        pc_single_res_frame, text="\nThe PC changed choice to No." + str(new_choice + 1)
    )
    text_box.place(relx=0.5, rely=0.2, anchor=CENTER)

    goat_img = load_image("assets/images/goat_image.jpg", 200, 150)
    car_img = load_image("assets/images/car_image.jpg", 200, 150)

    if ci == new_choice:
        Label(pc_single_res_frame, image=car_img).place(
            relx=0.5, rely=0.5, anchor=CENTER
        )
        play_sound("assets/sounds/ApplauseSound.wav")
        text_box_res = Label(pc_single_res_frame, text="PC Won!!!")

    else:
        Label(pc_single_res_frame, image=goat_img).place(
            relx=0.5, rely=0.5, anchor=CENTER
        )
        play_sound("assets/sounds/GoatSound.mp3")
        text_box_res = Label(pc_single_res_frame, text="PC Lost...")
    text_box_res.place(relx=0.5, rely=0.3, anchor=CENTER)

    Button(
        pc_single_res_frame,
        text="Restart",
        command=lambda: restart_program(pc_single_res_frame),
    ).place(relx=0.5, rely=0.7, anchor=CENTER)
    mainloop()
