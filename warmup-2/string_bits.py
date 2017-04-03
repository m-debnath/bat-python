def string_bits(str):
    """Given a string, return a new string made of every other char starting
    with the first, so "Hello" yields "Hlo"."""
    result = ""
    if len(str) > 1:
        for i in range(len(str)):
            if i % 2 == 0:
                result = result + str[i]
        return result
    else:
        return str