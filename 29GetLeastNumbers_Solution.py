

def GetLeastNumbers_Solution(nums, k):
    nums.sort()
    return nums[:k] if k <= len(nums) else []