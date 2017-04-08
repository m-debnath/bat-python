def count_code(str):
    """Return the number of times that the string "code" appears anywhere in 
    the given string, except we'll accept any letter for the 'd', so "cope" 
    and "cooe" count."""
    list = "abcdefghijklmnopqrstuvwxyz"
    count = 0
    for chr in list:
        find = "co" + chr + "e"
        count += str.count(find)
    return count