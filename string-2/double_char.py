def double_char(str):
    """Given a string, return a string where for every char in the original, 
    there are two chars."""
    res = ""
    for chr in str:
        res += (chr * 2)
    return res