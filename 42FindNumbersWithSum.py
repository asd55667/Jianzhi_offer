
def FindNumbersWithSum(nums, s):
    h = {}
    res = []
    for n in nums:
        if n not in h:
            h[s-n] = n
        else:
            res.append([h[n],n])
    if res:            
        res.sort(key=lambda x: x[0]*x[1])
        return res[0]
    return []

    
