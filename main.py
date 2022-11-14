from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from AlgoSetup import game_run, mh_problem_human_p1
import pygame
import random
# import os


# def restart():
#     root.destroy()
#     os.startfile("main.py")


def create_new_window(frame_destroy):
    frame_destroy.destroy()
    new_frame = Frame(width=650, height=500)
    new_frame.pack(fill="both", expand=True, padx=0, pady=0)
    new_frame.columnconfigure(0, weight=1)
    new_frame.columnconfigure(1, weight=1)
    new_frame.columnconfigure(2, weight=1)
    Label(new_frame, image=bg).place(x=0, y=0)
    return new_frame


def human_run():

    first_human_frame = create_new_window(frame)

    ttk.Label(first_human_frame, text="Make your choice").grid(column=1, row=0, pady=10)
    Label(first_human_frame, image=curtains_img_tk).grid(column=0, row=1)
    Label(first_human_frame, image=curtains_img_tk).grid(column=1, row=1)
    Label(first_human_frame, image=curtains_img_tk).grid(column=2, row=1)

    Button(
        first_human_frame,
        text="NO.1",
        command=lambda: human_sec_choice(0, first_human_frame),
    ).grid(column=0, row=2, pady=10)
    Button(
        first_human_frame,
        text="NO.2",
        command=lambda: human_sec_choice(1, first_human_frame),
    ).grid(column=1, row=2, pady=10)
    Button(
        first_human_frame,
        text="NO.3",
        command=lambda: human_sec_choice(2, first_human_frame),
    ).grid(column=2, row=2, pady=10)
    root.mainloop()


def human_sec_choice(first_choice, first_frame):
    exposed_goat_index, l1 = mh_problem_human_p1(first_choice)
    second_human_frame = create_new_window(first_frame)
    ttk.Label(second_human_frame, text="Now do you want to change your choice?").grid(
        column=1, row=0, pady=10
    )

    for i in range(3):
        if i == exposed_goat_index:
            image_label = Label(second_human_frame, image=goat_img_tk)
        else:
            image_label = Label(second_human_frame, image=curtains_img_tk)
            if i == 0:
                Button(
                    second_human_frame,
                    text="Change" if i != first_choice else "Stand",
                    command=lambda: human_results(
                        first_choice, 0, l1, second_human_frame
                    ),
                ).grid(column=i, row=2)
            elif i == 1:
                Button(
                    second_human_frame,
                    text="Change" if i != first_choice else "Stand",
                    command=lambda: human_results(
                        first_choice, 1, l1, second_human_frame
                    ),
                ).grid(column=i, row=2)
            else:
                Button(
                    second_human_frame,
                    text="Change" if i != first_choice else "Stand",
                    command=lambda: human_results(
                        first_choice, 2, l1, second_human_frame
                    ),
                ).grid(column=i, row=2)
        image_label.grid(column=i, row=1)
    root.mainloop()


def human_results(first_choice, second_choice, l1, second_human_frame):
    human_results_frame = create_new_window(second_human_frame)
    ci = l1.index("car")
    ttk.Label(
        human_results_frame, text="You Won!" if ci == second_choice else "You Lost!"
    ).place(relx=0.5, rely=0.2, anchor=CENTER)
    ttk.Label(
        human_results_frame,
        text="Choice changed"
        if first_choice != second_choice
        else "Choice not changed",
    ).place(relx=0.5, rely=0.25, anchor=CENTER)

    image_label = Label(
        human_results_frame, image=car_image_tk if ci == second_choice else goat_img_tk
    )
    image_label.place(relx=0.5, rely=0.5, anchor=CENTER)

    if ci == second_choice:
        play("Sounds/ApplauseSound.wav")
    else:
        play("Sounds/GoatSound.mp3")

    # Button(
    #     human_results_frame,
    #     text="Restart",
    #     command=lambda: restart()
    # ).place(relx=0.5, rely=0.7, anchor=CENTER)

    root.mainloop()


def pc_multirun():
    pc_multirun_frame = create_new_window(frame)
    ttk.Label(pc_multirun_frame, text="Times to run:").grid(column=1, row=6, pady=10)
    times_to_run = [("100", 100), ("1000", 1000), ("10,000", 10000), ("100,000", 100000)]
    v = IntVar()
    v.set(100)
    ttk.Button(pc_multirun_frame, text="Select", command=lambda: pc_multirun_res(pc_multirun_frame, v.get())).grid(column=1, row=1, pady=10)
    i = 0
    for times, val in times_to_run:
        b = ttk.Radiobutton(pc_multirun_frame, text=times, variable=v, command=v.get(), value=val)
        b.grid(column=1, row=7 + i)
        i += 1


def pc_multirun_res(pc_multirun_frame, n):
    pc_multirun_frame_res = create_new_window(pc_multirun_frame)
    text_box = ttk.Label(pc_multirun_frame_res, width=100, text="")
    text_box.grid(column=0, row=0)
    wins = game_run(n, False, text_box)
    play("Sounds/ApplauseSound.wav"if wins else "Sounds/GoatSound.mp3")
    image_label = Label(
        pc_multirun_frame_res, image=car_image_tk if wins else goat_img_tk
    )
    image_label.place(relx=0.5, rely=0.5, anchor=CENTER)

    ttk.Label(
            pc_multirun_frame_res, text="You Won!" if wins else "You Lost!"
        ).place(relx=0.5, rely=0.2, anchor=CENTER)
    ttk.Label(
        pc_multirun_frame_res,
        text="Choice changed"
    ).place(relx=0.5, rely=0.25, anchor=CENTER)


def pc_single_run():
    pc_single_frame = create_new_window(frame)
    choice = random.randint(0, 2)
    text_box = ttk.Label(pc_single_frame, text="\nThe PC choice was No." + str(choice+1))
    text_box.grid(column=1, row=0, pady=10)
    Label(pc_single_frame, image=curtains_img_tk).grid(column=0, row=1)
    Label(pc_single_frame, image=curtains_img_tk).grid(column=1, row=1)
    Label(pc_single_frame, image=curtains_img_tk).grid(column=2, row=1)
    Button(
        pc_single_frame,
        text="Next Step",
        command=lambda: pc_single_run_p2(
            pc_single_frame, choice
        ),
    ).grid(column=1, row=2, pady=10)


def pc_single_run_p2(pc_single_frame, choice):
    pc_single_p2_frame = create_new_window(pc_single_frame)
    exposed_goat, l1 = mh_problem_human_p1(choice)
    text_box = ttk.Label(pc_single_p2_frame,
                         text="\nThe PC first choice was No." + str(choice + 1)+"\nThe game show expose curtain NO."+str(exposed_goat+1))
    text_box.grid(column=1, row=0, pady=10)
    Label(pc_single_p2_frame, image=goat_img_tk).grid(column=exposed_goat, row=1)
    for i in range(3):
        if i != exposed_goat:
            Label(pc_single_p2_frame, image=curtains_img_tk).grid(column=i, row=1)

    print("old choice: " + str(choice))
    print("expose goat: " + str(exposed_goat))
    ci = l1.index("car")
    arr = [0, 1, 2]
    arr.remove(choice)
    arr.remove(exposed_goat)
    print("new choice: " + str(arr[0]))
    Button(
        pc_single_p2_frame,
        text="Next Step",
        command=lambda: pc_single_run_res(
            pc_single_p2_frame, arr[0], ci
        ),
    ).grid(column=1, row=2, pady=10)


def pc_single_run_res(pc_single_p2_frame, new_choice, ci):
    pc_single_res_frame = create_new_window(pc_single_p2_frame)

    text_box = ttk.Label(pc_single_res_frame,
                         text="\nThe PC changed choice to No." + str(new_choice+1))
    text_box.place(relx=0.5, rely=0.2, anchor=CENTER)

    if ci == new_choice:
        Label(pc_single_res_frame, image=car_image_tk).place(relx=0.5, rely=0.5, anchor=CENTER)
        play("Sounds/ApplauseSound.wav")
        text_box_res = ttk.Label(pc_single_res_frame, text="PC Won!!!")

    else:
        Label(pc_single_res_frame, image=goat_img_tk).place(relx=0.5, rely=0.5, anchor=CENTER)
        play("Sounds/GoatSound.mp3")
        text_box_res = ttk.Label(pc_single_res_frame, text="PC Lost...")
    text_box_res.place(relx=0.5, rely=0.3, anchor=CENTER)


def play(sound):
    pygame.mixer.music.load(sound)
    pygame.mixer.music.play(loops=0)


root = Tk()
root.title("Seminar")
root.geometry("650x500")
root.resizable(False, False)
pygame.mixer.init()

frame = Frame(root, width=650, height=500, background="#D3D3D3")
frame.pack(fill="both", expand=True, padx=0, pady=0)

bg_img = Image.open("bg_img.jpg")
bg_img = bg_img.resize((650, 500))
bg = ImageTk.PhotoImage(bg_img)

bg_label = Label(frame, image=bg)
bg_label.place(x=0, y=0)
frame.columnconfigure(0, weight=1)
frame.columnconfigure(1, weight=1)
frame.columnconfigure(2, weight=1)

ttk.Label(frame, text="Welcome To The Monty Hall Game").grid(column=1, row=0, pady=10)

curtains_img = Image.open("curtains_image.webp")
curtains_img = curtains_img.resize((200, 150))
curtains_img_tk = ImageTk.PhotoImage(curtains_img)
curtains_label_1 = Label(frame, image=curtains_img_tk)
curtains_label_1.grid(column=0, row=1)
curtains_label_2 = Label(frame, image=curtains_img_tk)
curtains_label_2.grid(column=1, row=1)
curtains_label_3 = Label(frame, image=curtains_img_tk)
curtains_label_3.grid(column=2, row=1)

goat_img = Image.open("goat_image.jpg")
goat_img = goat_img.resize((200, 150))
goat_img_tk = ImageTk.PhotoImage(goat_img)

car_image = Image.open("car_image.jpg")
car_image = car_image.resize((200, 150))
car_image_tk = ImageTk.PhotoImage(car_image)

ttk.Label(frame, text="Choose Game Type:").grid(column=1, row=3, pady=10)

ttk.Button(frame, text="PC Single-Run", command=pc_single_run).grid(
    column=0, row=4, pady=10
)
ttk.Button(frame, text="Statistics", command=pc_multirun).grid(
    column=1, row=4, pady=10
)
ttk.Button(frame, text="Human Run", command=human_run).grid(column=2, row=4, pady=10)

root.mainloop()
