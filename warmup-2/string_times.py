def string_times(str, n):
    """Given a string and a non-negative int n, return a larger string that is n copies of the original string."""
    if n < 0:
        return str
    else:
        return str * n