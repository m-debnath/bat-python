def string_bits(str):
    result = ""
    if len(str) > 1:
        for i in range(len(str)):
            if i % 2 == 0:
                result = result + str[i]
        return result
    else:
        return str