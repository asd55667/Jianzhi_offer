# xor
def FindNumsAppearOnce(nums):
    def IsIdxBit1(n, idx):
        n >>= idx
        return n & 1

    if not nums: return []
    res = 0
    for n in nums:
        res ^= n
    idx = 0
    while (res & 1 ) == 0:
        res >>= 1
        idx += 1

    a, b = 0, 0
    for n in nums:
        if IsIdxBit1(n, idx):
            a ^= n 
        else: 
            b ^= n 
    return [a,b]



def FindNumsAppearOnce(nums):
    nums.sort()
    res = []
    for n in nums:
        if n in res:
            res.pop()
            continue
        res.append(n)
    return res


print(FindNumsAppearOnce([1,2,2]))