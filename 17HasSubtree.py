class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None



def HasSubtree(s, t):
    def convert(p):
        return str(p.val)+convert(p.left) + convert(p.right) if p else ''
    return convert(t) in convert(s) if t else None
    


    
def HasSubtree(s, t):
    def isSub(s,t):
        if not t: return True
        if not s: return False
        return s.val == t.val and isSub(s.left, t.left) and isSub(s.right, t.right)
        
    if not s or not t:
        return False
    if isSub(s,t):
        return True
    else:
        return HasSubtree(s.left, t) or HasSubtree(s.right, t)




