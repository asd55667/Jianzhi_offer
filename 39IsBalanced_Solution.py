
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def IsBalanced_Solution(t):
    
    def TreeDepth(t):
        if not t: return 0
        return 1 + max(TreeDepth(t.left), TreeDepth(t.right))

    if not t: return True
    l = TreeDepth(t.left)
    r = TreeDepth(t.right)
    if abs(l-r) > 1:
        return False
    return IsBalanced_Solution(t.left) and IsBalanced_Solution(t.right)

