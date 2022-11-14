from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from AlgoSetup import game_run, mh_problem_human_p1
import pygame

# add sounds
# 3 options:
# 1. pc runs 100/1000... times and show statistic ---- check
# 2. human run --- pending
# 3. single pc run and show steps. --- check


def create_new_window(frame_destroy):
    frame_destroy.destroy()
    new_frame = Frame(width=650, height=500)
    new_frame.pack(fill="both", expand=True, padx=0, pady=0)
    return new_frame


def human_run():
    first_human_frame = create_new_window(frame)
    ttk.Label(first_human_frame, text="Make your choice").grid(column=1, row=0, pady=10)
    curtains_img_1 = Image.open("curtains_image.webp")
    curtains_img_1 = curtains_img_1.resize((200, 150))
    curtains_img_tk = ImageTk.PhotoImage(curtains_img_1)
    curtains_label_1 = Label(first_human_frame, image=curtains_img_tk)
    curtains_label_1.grid(column=0, row=1)
    curtains_label_2 = Label(first_human_frame, image=curtains_img_tk)
    curtains_label_2.grid(column=1, row=1)
    curtains_label_3 = Label(first_human_frame, image=curtains_img_tk)
    curtains_label_3.grid(column=2, row=1)
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

    curtains_img = Image.open("curtains_image.webp")
    curtains_img = curtains_img.resize((200, 150))
    curtains_img_tk = ImageTk.PhotoImage(curtains_img)

    goat_img = Image.open("goat_image.jpg")
    goat_img = goat_img.resize((200, 150))
    goat_img_tk = ImageTk.PhotoImage(goat_img)

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
    ).grid(column=1, row=0, pady=10)
    ttk.Label(
        human_results_frame,
        text="Choice changed"
        if first_choice != second_choice
        else "Choice not changed",
    ).grid(column=1, row=1, pady=10)

    car_image = Image.open("car_image.jpg")
    car_image = car_image.resize((200, 150))
    car_image_tk = ImageTk.PhotoImage(car_image)

    goat_img = Image.open("goat_image.jpg")
    goat_img = goat_img.resize((200, 150))
    goat_img_tk = ImageTk.PhotoImage(goat_img)

    image_label = Label(
        human_results_frame, image=car_image_tk if ci == second_choice else goat_img_tk
    )
    image_label.grid(column=1, row=2)

    if ci == second_choice:
        play("Sounds/ApplauseSound.wav")
    else:
        play("Sounds/GoatSound.mp3")

    root.mainloop()


def pc_multirun():
    selected_change = change1.get()
    selected_change = False if selected_change == 0 else True
    n = v.get()
    pc_multirun_frame = create_new_window(frame)
    text_box = ttk.Label(pc_multirun_frame, width=100, text="")
    text_box.grid(column=0, row=0)
    sound_to_play = game_run(n, False, selected_change, text_box)
    if sound_to_play:
        play("Sounds/ApplauseSound.wav")
    else:
        play("Sounds/GoatSound.mp3")


def pc_single_run():
    selected_change = change2.get()
    selected_change = False if selected_change == 0 else True
    pc_single_frame = create_new_window(frame)
    text_box = ttk.Label(pc_single_frame, width=100, text="")
    text_box.grid(column=0, row=0, padx=10, pady=10)
    sound_to_play = game_run(1, True, selected_change, text_box)
    if sound_to_play:
        play("Sounds/ApplauseSound.wav")
    else:
        play("Sounds/GoatSound.mp3")


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

curtains_img = Image.open("curtains_image.webp")
bg = ImageTk.PhotoImage(curtains_img)
bg_label = Label(frame, image=bg)
bg_label.place(x=0, y=0)
frame.columnconfigure(0, weight=1)
frame.columnconfigure(1, weight=1)
frame.columnconfigure(2, weight=1)

# play("Sounds/OpeningSound.wav")

ttk.Label(frame, text="Welcome To The Monty Hall Game").grid(column=1, row=0, pady=10)
ttk.Label(frame, text="Choose Game Type:").grid(column=1, row=1, pady=10)

ttk.Button(frame, text="PC Single-Run", command=pc_single_run).grid(
    column=0, row=2, pady=10
)
ttk.Button(frame, text="PC Multi-Run", command=pc_multirun).grid(
    column=1, row=2, pady=10
)
ttk.Button(frame, text="Human Run", command=human_run).grid(column=2, row=2, pady=10)

ttk.Label(frame, text="Times to run:").grid(column=1, row=6, pady=10)
ttk.Label(frame, text="PC behaviour:").grid(column=0, row=3, pady=10)
ttk.Label(frame, text="PC behaviour:").grid(column=1, row=3, pady=10)

times_to_run = [("100", 100), ("1000", 1000), ("10,000", 10000)]
v = IntVar()
v.set(100)

i = 0
for times, val in times_to_run:
    b = ttk.Radiobutton(frame, text=times, variable=v, command=v.get(), value=val)
    b.grid(column=1, row=7 + i)
    i += 1


options = [("Always Change", 1), ("Never Change", 0)]
change1 = IntVar()
change2 = IntVar()

i = 0
for option, val in options:
    b1 = ttk.Radiobutton(
        frame, text=option, variable=change1, command=change1.get(), value=val
    )
    b2 = ttk.Radiobutton(
        frame, text=option, variable=change2, command=change2.get(), value=val
    )
    b1.grid(column=1, row=4 + i)
    b2.grid(column=0, row=4 + i)
    i += 1


root.mainloop()
