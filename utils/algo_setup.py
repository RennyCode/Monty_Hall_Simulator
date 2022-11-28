import random


def mh_problem() -> tuple[int, int, int]:
    l1 = ["goat", "car", "goat"]
    random.shuffle(l1)
    l2 = [0, 1, 2]
    ci = l1.index("car")
    fc = random.randint(0, 2)
    l3 = []
    for i in range(len(l1)):
        if i != ci:
            l3.append(i)
    s = ""
    for x in l3:
        s = s + " " + str(x)
        if x != fc:
            k = x
    for i in range(len(l2)):
        if l2[i] != fc and l2[i] != k:
            sc = i
            break
    return ci, fc, sc


def mh_problem_partial(choice_index: int) -> tuple[int, list[str]]:
    obj_list = ["goat", "car", "goat"]
    random.shuffle(obj_list)
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


def statistics_calculate(n: int) -> tuple[bool, int, int, int]:
    wins = 0
    losses = 0
    for i in range(n):
        ci, fc, sc = mh_problem()
        if ci == sc:
            wins += 1
        elif fc == ci:
            losses += 1
    if wins > losses:
        return True, n, wins, losses
    else:
        return False, n, wins, losses
