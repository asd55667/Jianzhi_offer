def FindContinuousSequence(s):
    res = []
    max_len = int((s*2)**0.5)
    for length in reversed(range(2, max_len+1)):
        median = s // length
        delta = length // 2
        if length & 1 and s % length == 0:
            res.append(list(range(median-delta, median+delta+1)))
        elif (s % length) * 2 == length:
            res.append(list(range(median-delta+1, median+delta+1)))
    return res

# two pointer
def FindContinuousSequence(s):
    res  = []
    l, r = 1, 2
    while l < r:
        tmp = (l+r)*(r-l+1)//2
        if tmp == s:
            res.append(list(range(l,r+1)))
            r+=1
        elif tmp > s:
            l+=1
        else:
            r+=1
    return res

print(FindContinuousSequence(100))