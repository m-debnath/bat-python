def sum2(nums):
    """Given an array of ints, return the sum of the first 2 elements in the
     array. If the array length is less than 2, just sum up the elements that
     exist, returning 0 if the array is length 0."""
    result = 0
    i = 0
    for num in nums:
        result = result + num
        i = i + 1
        if i == 2:
            break
    return result