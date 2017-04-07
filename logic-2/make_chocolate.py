def make_chocolate(small, big, goal):
    sval = 1
    bval = 5
    if big * bval == goal:
        return 0
    elif big * bval < goal:
        if ((goal - (big * bval)) % sval) == 0:
            if (goal - (big * bval)) <= (small * sval):
                return (goal - (big * bval)) / sval
        return -1
    else:
        if (goal % bval) % sval == 0:
            if (goal % bval) <= (small * sval):
                return (goal % bval) / sval
        return -1