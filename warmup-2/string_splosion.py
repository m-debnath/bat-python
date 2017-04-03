def string_splosion(str):
    """Given a non-empty string like "Code" return a string like "CCoCodCode"."""
    result=""
    for i in range(len(str)):
        result = result + str[:i+1]
    return result