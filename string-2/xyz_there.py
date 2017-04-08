def xyz_there(str):
    """Return True if the given string contains an appearance of "xyz" where 
    the xyz is not directly preceeded by a period (.). So "xxyz" counts but 
    "x.xyz" does not."""
    count_1, count_2 = 0, 0
    count_1 = str.count("xyz")
    count_2 = str.count(".xyz")
    if count_1 == 0: return False
    if count_1 > 0:
        if count_1 > count_2: return True
    return False 