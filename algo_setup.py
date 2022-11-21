import random


def mh_problem(should_print, text_box):
    l1 = ["goat", "car", "goat"]
    random.shuffle(l1)
    if should_print:
        my_text = (
            text_box["text"] + "\npartitions: " + l1[0] + " " + l1[1] + " " + l1[2]
        )
        text_box.config(text=my_text)
    l2 = [0, 1, 2]
    ci = l1.index("car")
    if should_print:
        my_text = text_box["text"] + "\nthe car is behind partition number: " + str(ci)
        text_box.config(text=my_text)
    fc = random.randint(0, 2)
    if should_print:
        my_text = (
            text_box["text"] + "\nfirst choice: " + str(l1[fc]) + "   index: " + str(fc)
        )
        text_box.config(text=my_text)
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
        my_text = text_box["text"] + "\nindices of goats partition: " + s
        text_box.config(text=my_text)
    if should_print:
        my_text = text_box["text"] + "\nindex of exposed goat partition: " + str(k)
        text_box.config(text=my_text)
    for i in range(len(l2)):
        if l2[i] != fc and l2[i] != k:
            sc = i
            break
    if should_print:
        my_text = (
            text_box["text"]
            + "\nsecond choice: "
            + str(l1[sc])
            + "  index of second choice: "
            + str(sc)
        )
        text_box.config(text=my_text)
    return ci, fc, sc


def mh_problem_partial(choice_index):
    obj_list = ["goat", "car", "goat"]
    random.shuffle(obj_list)
    print(obj_list)
    l2 = [0, 1, 2]
    ci = obj_list.index("car")
    l3 = []
    for i in range(len(obj_list)):
        if i != ci:
            l3.append(i)
    s = ""
    for x in l3:
        s = s + " " + str(x)
        if x != choice_index:
            exposed_goat_index = x
    for i in range(len(l2)):
        if l2[i] != choice_index and l2[i] != exposed_goat_index:
            sc = i
            break
    return exposed_goat_index, obj_list


def game_run(n, should_print, text_box):
    wins = 0
    losses = 0
    for i in range(n):
        if should_print:
            print("\ngame number: " + str(i + 1))
        ci, fc, sc = mh_problem(should_print, text_box)
        if ci == sc:
            wins += 1
        elif fc == ci:
            losses += 1

    my_text = (
        text_box["text"]
        + "\n\nnumber of games: "
        + "{0:,d}".format(n)
        + "\nnumber of wins   because of choice change: "
        + "{0:,d}".format(wins)
        + "\nnumber of losses because of choice change: "
        + "{0:,d}".format(losses)
        + "\nwin/lose ratio: "
        + "{:.2f}".format(wins/losses)
    )
    text_box.config(text=my_text)
    if format(wins) > format(losses):
        return True
    else:
        return False
