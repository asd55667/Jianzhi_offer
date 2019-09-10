class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def PrintFromTopToBottom(root):
    if not root: return None
    q = [root]
    vals = []
    while q:
        n = len(q)
        for _ in range(n):
            node = q.pop(0)
            vals.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
    return vals
