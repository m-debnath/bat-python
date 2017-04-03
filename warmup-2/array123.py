def array123(nums):
    """Given an array of ints, return True if the sequence of numbers
     1, 2, 3 appears in the array somewhere."""
    list = [1, 2, 3]
    indx = 3
    if len(nums) < indx:
        return False
    for i in range(len(nums)-(indx-1)):
        if nums[i:i+3] == list:
            return True
    return False