


def MoreThanHalfNum_Solution(nums):
    nums.sort()
    mid = nums[len(nums) // 2]
    count = 0
    for n in nums:
        if n == mid:
            count += 1
    return mid if count > len(nums) // 2 else 0
