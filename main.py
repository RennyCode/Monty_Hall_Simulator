from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import random

# add sounds
# 3 options:
# 1. pc runs 100/1000... times and show statistic
# 2. human run
# 3. single pc run and show steps.

def mpProblem(should_print, text_box):
    l1 = ["goat", "car", "goat"]
    random.shuffle(l1)
    if should_print:
        print("\npartitions: " + l1[0]
                       + " " + l1[1] + " " + l1[2])
    l2 = [0, 1, 2]
    ci = l1.index("car")
    if should_print:
        print("\nthe car is behind partition number: "
                      + str(ci))
    fc = random.randint(0, 2)
    if should_print:
        print("\nfirst choice: " + str(l1[fc])
                      +  "   index: " + str(fc))
    l3 = []
    for i in range(len(l1)):
        if i != ci:
            l3.append(i)
    s = ""
    for x in l3:
      s = s + " " + str(x)
      if x != fc:
          k = x
    if should_print:
        print("\nindices of goats partition: " + s)
    if should_print:
        print("\nindex of exposed goat partition: "
                      + str(k))
    for i in range(len(l2)):
        if l2[i] != fc and l2[i] != k:
            sc = i
            break
    if should_print:
        print("\nsecond choice: " + str(l1[sc])
                      + "  index of second choice: " + str(sc))
    return ci, fc, sc


def game_run(n, should_print, changes, text_box):
    # outfile = open("mhResults.txt", 'w')
    wins = 0
    losses = 0
    for i in range(n):
        if should_print:
            print("\ngame number: " + str(i + 1))
            # my_text = text_box["text"] + "\ngame number: " + str(i + 1)
            # text_box.config(text=my_text)
        ci, fc, sc = mpProblem(should_print, text_box)
        if changes:
            if ci == sc:
                wins += 1
            elif fc == ci:
                losses += 1
        else:
            if ci == sc:
                losses += 1
            elif fc == ci:
                wins += 1

    my_text = text_box["text"] + "\n\nnumber of games: " + "{0:,d}".format(i+1) + "\nnumber of wins   because of choice change: "+ "{0:,d}".format(wins)+ "\nnumber of losses because of choice change: "+ "{0:,d}".format(losses)
    text_box.config(text=my_text)

    # print("\n\nnumber of games: "
    #       + "{0:,d}".format(i+1)
    #       + "\nnumber of wins   because of choice change: "
    #       + "{0:,d}".format(wins)
    #       + "\nnumber of losses because of choice change: "
    #       + "{0:,d}".format(losses))
    # outfile.close()


def create_new_window():
    root.destroy()
    new_root = Tk()
    new_root.geometry("635x500")
    return new_root


def human_run():
    create_new_window()
    car_img = Image.open("car_image.jpg")
    car_img = car_img.resize((200, 150))
    car_imgTK = ImageTk.PhotoImage(car_img)
    car_label = Label(root, image=car_imgTK)
    car_label.place(x=0, y=0)
    goat_img = Image.open("goat_image.jpg")
    goat_img = goat_img.resize((200, 150))
    goat_imgTK = ImageTk.PhotoImage(goat_img)
    goat_label = Label(root, image=goat_imgTK)
    goat_label.place(x=0, y=0)
    ttk.Label(root, image=car_imgTK).grid(column=0, row=3)
    ttk.Label(root, image=goat_imgTK).grid(column=1, row=3)


def pc_changes():
    new_root = create_new_window()
    text_box = ttk.Label(new_root, width=100, text="")
    text_box.grid(column=0, row=0)
    game_run(100, True, True, text_box)


def pc_no_changes():
    new_root = create_new_window()
    text_box = ttk.Label(new_root, width=100, text="")
    text_box.grid(column=0, row=0)
    game_run(100, True, False, text_box)


root = Tk()
root.title("Seminar")
root.geometry("800x500")
curtains_img = Image.open("curtains_image.webp")
bg = ImageTk.PhotoImage(curtains_img)
bg_label = Label(root, image=bg)
bg_label.place(x=0, y=0)
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)
ttk.Label(root, text="Welcome To The Monty Hall Game").grid(column=1, row=0, pady=5, columnspan=2)
ttk.Label(root, text="Choose Game Type:").grid(column=1, row=1, pady=20, columnspan=2)
ttk.Button(root, text="Human Run", command=human_run).grid(column=4, row=2, pady=10)
ttk.Button(root, text="PC Multi-Run", command=pc_changes).grid(column=2, row=2, pady=10, columnspan=2, sticky=W)
ttk.Button(root, text="PC Single-Run", command=pc_no_changes).grid(column=0, row=2, columnspan=2)
timesToRunText = ttk.Label(root, text="Times To Run: ")
timesToRunText.grid(column=1, row=3, sticky=E)
timesToRun = ttk.Combobox(root, textvariable="Times To Run")
timesToRun["values"] = (100, 1000, 10000)
timesToRun.grid(column=2, row=3, sticky=W)
changeText = ttk.Label(root, text="Choice")
changeText.grid(column=1, row=4, sticky=E)
change = ttk.Combobox(root, textvariable="Choice")
change["values"] = ("Always Changes", "Never Changes")
change.grid(column=2, row=4, sticky=W)

changeText = ttk.Label(root, text="Choice")
changeText.grid(column=0, row=4, sticky=E)
change = ttk.Combobox(root, textvariable="Choice")
change["values"] = ("Change", "Don't Change")
change.grid(column=1, row=4, sticky=W)

root.mainloop()

