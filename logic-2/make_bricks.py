def make_bricks(small, big, goal):
    """We want to make a row of bricks that is goal inches long. We have a 
    number of small bricks (1 inch each) and big bricks (5 inches each). 
    Return True if it is possible to make the goal by choosing from the given 
    bricks. This is a little harder than it looks and can be done without any loops."""
    slen = 1
    blen = 5
    if big * blen == goal:
        return True
    elif small * slen == goal:
        return True
    elif big * blen < goal:
        if ((goal - (big * blen)) % slen) == 0:
            return (goal - (big * blen)) <= (small * slen)
        return False
    else:
        if (goal % blen) % slen == 0:
            return (goal % blen) <= (small * slen)
        return False