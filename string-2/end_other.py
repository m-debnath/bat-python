def end_other(a, b):
    """Given two strings, return True if either of the strings appears at the 
    very end of the other string, ignoring upper/lower case differences (in 
    other words, the computation should not be "case sensitive")."""
    la = a.lower()
    lb = b.lower()
    if len(la) > len(lb):
        return (la[len(la)-len(lb):] == lb)
    return (lb[len(lb)-len(la):] == la)