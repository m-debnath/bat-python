def first_half(str):
    """Given a string of even length, return the first half.
     So the string "WooHoo" yields "Woo"."""
    half = len(str)//2
    return str[:half]