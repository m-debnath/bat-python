def array_front9(nums):
    """Given an array of ints, return True if one of the first 4 elements
     in the array is a 9. The array length may be less than 4."""
    src = 9
    lmt = 4
    for i in range(len(nums)):
        if nums[i] == src:
            return True
        if i == lmt-1:
            return False
    else:
        return False