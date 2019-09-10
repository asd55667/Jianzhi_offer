

def GetUglyNumber_Solution(idx):
    if idx < 7: return idx
    res = [1] * idx
    t2=t3=t5 = 0
    for i in range(1, idx):
        res[i]  = min(res[t2]*2, min(res[t3]*3, res[t5]*5))
        if res[i] == res[t2]*2: t2 += 1
        if res[i] == res[t3]*3: t3 += 1
        if res[i] == res[t5]*5: t5 += 1
    return res[idx-1]




print(GetUglyNumber_Solution(7))






