class Solution:
    s = ''
    def FirstAppearingOnce():
        res = []
        dup = set()
        for c in self.s:
            if c in res:
                dup.add(c)
            else:
                res.append(c)
        for c in res:
            if c not in dup:
                return c
        return '#'

    def Insert(char):   
        self.s += char