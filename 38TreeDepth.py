class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def TreeDepth(t):
    if not t: return 0
    s = [(t,1)]
    m = 1
    while s:
        node, depth = s.pop()
        if depth > m:
            m = depth
        if node.left:
            s.append((node.left, depth+1))
        if node.right:
            s.append((node.right, depth+1))
    return m

def TreeDepth(t):
    if not t: return 0
    return 1 + max(TreeDepth(t.left), TreeDepth(t.right))
    