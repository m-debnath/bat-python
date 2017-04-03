def array_count9(nums):
    """Given an array of ints, return the number of 9's in the array."""
    src = 9
    count = 0
    for num in nums:
        if num == src:
            count = count + 1
    return count