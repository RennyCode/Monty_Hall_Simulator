from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import random

def mpProblem(outfile, print):
    l1 = ["goat", "car", "goat"]
    random.shuffle(l1)
    if print:
        outfile.write("\npartitions: " + l1[0]
                      + " " + l1[1] + " " + l1[2])
    l2 = [0, 1, 2]
    ci = l1.index("car")
    if print:
        outfile.write("\nthe car is behind partition number: "
                      + str(ci))
    fc = random.randint(0, 2)
    if print:
        outfile.write("\nfirst choice: " + str(l1[fc])
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
    if print:
        outfile.write("\nindices of goats partition: " + s)
    if print:
        outfile.write("\nindex of exposed goat partition: "
                      + str(k))
    for i in range(len(l2)):
        if l2[i] != fc and l2[i] != k:
            sc = i
            break
    if print:
        outfile.write("\nsecond choice: " + str(l1[sc])
                      + "  index of second choice: " + str(sc))
    return ci, fc, sc

def game_run(n, print):
    outfile = open("mhResults.txt", 'w')
    wins = 0
    losses = 0
    for i in range(n):
        if print:
            outfile.write(("\ngame number: " + str(i + 1)))
        ci, fc, sc = mpProblem(outfile, print)
        if ci == sc:
            wins += 1
        elif fc == ci:
            losses += 1

    outfile.write("\n\nnumber of games: "
          + "{0:,d}".format(i+1)
          + "\nnumber of wins   because of choice change: "
          + "{0:,d}".format(wins)
          + "\nnumber of losses because of choice change: "
          + "{0:,d}".format(losses))

    outfile.close()


root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
root.title("Seminar")
ttk.Label(frm, text="Choose Game Type:").grid(column=1, row=0)
ttk.Button(frm, text="Human", command=root.destroy).grid(column=2, row=1)
ttk.Button(frm, text="PC", command=root.destroy).grid(column=0, row=1)
car_img = Image.open("car_image.jpg")
car_img = car_img.resize((200, 150))
car_imgTK = ImageTk.PhotoImage(car_img)
goat_img = Image.open("goat_image.jpg")
goat_img = goat_img.resize((200, 150))
goat_imgTK = ImageTk.PhotoImage(goat_img)
curtains_img = Image.open("curtains_image.webp")
curtains_img = curtains_img.resize((200, 150))
curtains_imgTK = ImageTk.PhotoImage(curtains_img)
ttk.Label(frm, image=car_imgTK).grid(column=0, row=3)
ttk.Label(frm, image=goat_imgTK).grid(column=1, row=3)
ttk.Label(frm, image=curtains_imgTK).grid(column=2, row=3)
root.mainloop()

