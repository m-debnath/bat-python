def centered_average(nums):
    nmin = nums[0]
    nmax = 0
    for num in nums:
        nmin = min(nmin, num)
        nmax = max(num, nmax)
    imin = nums.index(nmin)
    nums.pop(imin)
    imax = nums.index(nmax)
    nums.pop(imax)
    sum = 0
    for num in nums:
        sum += num
    avg = sum / len(nums)
    return avg