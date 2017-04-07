def round_sum(a, b, c):
    return round10(a) + round10(b) + round10(c)
def round10(num):
    if num % 10 >= 5:
        return (10 * ((num // 10) + 1))
    else:
        return (10 * (num // 10))