def not_string(str):
    """Given a string, return a new string where "not " has been added to the front. However, if the string already begins with "not", return the string unchanged."""
    if str[:3] == 'not':
        return str[:]
    else:
        return 'not ' + str[:]