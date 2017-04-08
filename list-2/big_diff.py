def big_diff(nums):
    """Given an array length 1 or more of ints, return the difference between 
    the largest and smallest values in the array. Note: the built-in 
    min(v1, v2) and max(v1, v2) functions return the smaller or larger of two 
    values."""
    nmin = nums[0]
    nmax = 0
    for num in nums:
        nmin = min(nmin, num)
        nmax = max(num, nmax)
    return abs(nmax - nmin)