def front_times(str, n):
    """Given a string and a non-negative int n, we'll say that the front of
    the string is the first 3 chars, or whatever is there if the string is
    less than length 3. Return n copies of the front."""
    front_len = 3
    if front_len > len(str):
        front = str
    else:
        front = str[:front_len]
    return front*n