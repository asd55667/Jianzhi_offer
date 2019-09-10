

def VerifySquenceOfBST(s):
    def h(s):
        if not s: return True
        root = s.pop()
        if s and s[0] > root:
            l = []
            r = s
        else:
            r = []
            for i in range(len(s)):
                if s[i] > root:
                    l = s[:i]
                    r = s[i:]
                    break
        for v in r:
            if v < root: return False
        return h(l) and h(r)
    
    if not s: return False
    return h(s)



def VerifySquenceOfBST(s):
    def judge(s, l, r):
        if l >= r: return True
        i = r 
        while i > 0 and s[i-1] > s[r]: 
            i -= 1
        for j in range(0, i):
            if s[j] > s[r]: return False
        return judge(s,l, i-1) and judge(s,i, r-1)
    if not s: return False
    return judge(s, 0, len(s)-1)

print(VerifySquenceOfBST([4,8,6,12,16,14,10]))