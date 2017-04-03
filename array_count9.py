def array_count9(nums):
    src = 9
    count = 0
    for num in nums:
        if num == src:
            count = count + 1
    return count