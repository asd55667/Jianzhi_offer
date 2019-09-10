
def FindGreatestSumOfSubArray(nums):
    pre = m = nums[0] 
    for n in nums[1:]:
        pre = max(pre+n,n)
        m = max(m,pre)
    return m
        

print(FindGreatestSumOfSubArray([1,-2,3,10,-4,7,2,-5]))
#[6,-3,-2,7,-15,1,2,2]
#[-2,-8,-1,-5,-9]