def array_front9(nums):
    src = 9
    lmt = 4
    for i in range(len(nums)):
        if nums[i] == src:
            return True
        if i == lmt-1:
            return False
    else:
        return False