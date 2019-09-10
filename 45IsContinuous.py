def IsContinuous(nums):
    if len(nums) != 5: return False
    nums.sort()
    for i in range(len(nums)):
        if nums[i] != 0:
            break
    if len(set(nums[i:])) != len(nums[i:]):
        return False
    if nums[-1]-nums[i] < 5:
        return True
    return False