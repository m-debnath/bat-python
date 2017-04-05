def without_end(str):
    """Given a string, return a version without the first and last char,
     so "Hello" yields "ell". The string length will be at least 2."""
    return str[1:len(str)-1]