from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from AlgoSetup import game_run
import pygame

# add sounds
# 3 options:
# 1. pc runs 100/1000... times and show statistic ---- check
# 2. human run --- pending
# 3. single pc run and show steps. --- check


def create_new_window():
    root.destroy()
    new_root = Tk()
    new_root.title("Seminar")
    new_root.geometry("650x500")
    new_root.resizable(False, False)
    return new_root


def human_run():
    new_root = create_new_window()

    curtains = Image.open("curtains_image.webp")
    c = ImageTk.PhotoImage(curtains)
    c_label = Label(new_root, image=c)
    c_label.place(x=0, y=0)

    car_img = Image.open("car_image.jpg")
    car_img = car_img.resize((200, 150))
    car_img_tk = ImageTk.PhotoImage(car_img)
    car_label = Label(new_root, image=car_img_tk)
    car_label.grid(column=0, row=0)
    goat_img = Image.open("goat_image.jpg")
    goat_img = goat_img.resize((200, 150))
    goat_img_tk = ImageTk.PhotoImage(goat_img)
    goat_label = Label(new_root, image=goat_img_tk)
    goat_label.grid(column=0, row=0)


def pc_multirun():
    selected_change = change1.get()
    selected_change = False if selected_change == 0 else True
    n = v.get()
    new_root = create_new_window()
    text_box = ttk.Label(new_root, width=100, text="")
    text_box.grid(column=0, row=0)
    sound_to_play = game_run(n, False, selected_change, text_box)
    if sound_to_play:
        play("Sounds/ApplauseSound.wav")
    else:
        play("Sounds/GoatSound.mp3")


def pc_single_run():
    selected_change = change2.get()
    selected_change = False if selected_change == 0 else True
    new_root = create_new_window()
    new_root.title("Seminar")
    new_root.geometry("650x500")
    new_root.resizable(False, False)
    text_box = ttk.Label(new_root, width=100, text="")
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


curtains_img = Image.open("curtains_image.webp")
bg = ImageTk.PhotoImage(curtains_img)
bg_label = Label(root, image=bg)
bg_label.place(x=0, y=0)
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)

# play("Sounds/OpeningSound.wav")

ttk.Label(root, text="Welcome To The Monty Hall Game").grid(column=1, row=0, pady=10)
ttk.Label(root, text="Choose Game Type:").grid(column=1, row=1, pady=10)

ttk.Button(root, text="PC Single-Run", command=pc_single_run).grid(column=0, row=2, pady=10)
ttk.Button(root, text="PC Multi-Run", command=pc_multirun).grid(column=1, row=2, pady=10)
ttk.Button(root, text="Human Run", command=human_run).grid(column=2, row=2, pady=10)

ttk.Label(root, text="Times to run:").grid(column=1, row=6, pady=10)
ttk.Label(root, text="PC behaviour:").grid(column=0, row=3, pady=10)
ttk.Label(root, text="PC behaviour:").grid(column=1, row=3, pady=10)

times_to_run = [("100", 100), ("1000", 1000), ("10,000", 10000)]
v = IntVar()
v.set(100)

i = 0
for times, val in times_to_run:
    b = ttk.Radiobutton(root, text=times, variable=v, command=v.get(), value=val)
    b.grid(column=1, row=7 + i)
    i += 1


options = [("Always Change", 1), ("Never Change", 0)]
change1 = IntVar()
change2 = IntVar()

i = 0
for option, val in options:
    b1 = ttk.Radiobutton(root, text=option, variable=change1, command=change1.get(), value=val)
    b2 = ttk.Radiobutton(root, text=option, variable=change2, command=change2.get(), value=val)
    b1.grid(column=1, row=4 + i)
    b2.grid(column=0, row=4 + i)
    i += 1


root.mainloop()

