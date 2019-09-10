import sys
sys.setrecursionlimit(4000)

def LastRemaining_Solution(n, m):
    def runCycle(nums, m):
        if len(nums) == 1: return nums[0]
        m_ = (m-1) % len(nums)
        return runCycle(nums[m_+1:]+nums[:m_], m)
    if n < 1: return -1
    return runCycle(list(range(n)), m)
    
def LastRemaining_Solution(n,m):
    if n < 1: return n-1
    # 第二轮重新编号的时候，相当于把每个人的编号都减了m
    return (LastRemaining_Solution(n-1,m) + m) % n  

def LastRemaining_Solution(n, m):
    con = list(range(n))
        
    final = -1
    start = 0
    while con:
        k = (start + m - 1) % n
        final = con.pop(k)
        n -= 1
        start = k            
    return final
  

print(LastRemaining_Solution(5,3))