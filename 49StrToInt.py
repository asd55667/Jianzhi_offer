
def StrToInt(s):
    if not s: return 0
    if len(s) == 1 and not s[0].isdigit(): return 0        
    
    if s[0] not in ['+', '-'] and not s[0].isdigit(): return 0
    
    sign = 1
    if s[0] == '-': sign = -1
    
    for char in s[1:]:
        if not char.isdigit(): 
            return 0
    
    def atoi(s):
        if s[0] in ['+', '-']: s = s[1:]
        res = 0
        for i in range(len(s)):
            d = ord(s[i])-ord('0')
            res += 10**(len(s)-i-1) * d
        return res
    return sign * atoi(s)
    

print(StrToInt('123'))    