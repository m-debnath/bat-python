def caught_speeding(speed, is_birthday):
    """You are driving a little too fast, and a police officer stops you. 
    Write code to compute the result, encoded as an int value: 
    0=no ticket, 1=small ticket, 2=big ticket. If speed is 60 or less, the 
    result is 0. If speed is between 61 and 80 inclusive, the result is 1. 
    If speed is 81 or more, the result is 2. Unless it is your birthday -- on 
    that day, your speed can be 5 higher in all cases."""
    if is_birthday:
        limit_1, limit_2 = 65, 85
    else:
        limit_1, limit_2 = 60, 80
    if speed <= limit_1:
        return 0
    elif speed > limit_1 and speed <= limit_2:
        return 1
    else:
        return 2