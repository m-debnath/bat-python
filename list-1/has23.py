def has23(nums):
    """Given an int array length 2, return True if it contains a 2 or a 3."""
    for num in nums:
        if num == 2 or num == 3:
            return True
    return False