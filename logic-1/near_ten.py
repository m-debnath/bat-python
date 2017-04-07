def near_ten(num):
    """Given a non-negative number "num", return True if num is within 2 of 
    a multiple of 10. Note: (a % b) is the remainder of dividing a by b, so 
    (7 % 5) is 2."""
    result = num % 10
    return (result >= 8 or result <= 2)