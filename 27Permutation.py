
def Permutation(ss):

    if len(ss) == 1:
        return ss
    res = []
    ss = ''.join(sorted(ss))        
    for i in range(len(ss)):
        c = ss[i]
        for p in Permutation(ss[:i]+ss[i+1:]):
            if c+p in res:
                continue            
            res.append(c + p)
            
    return res

print(Permutation('aab'))




        
        