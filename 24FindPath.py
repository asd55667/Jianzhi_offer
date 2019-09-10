class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def FindPath(root, n):
    if not root: return []
    from collections import deque
    s = [(root, [root.val])]
    res = deque()
    while s:
        node, p = s.pop()
        if sum(p) == n and not node.left and node.right:
            res.appendleft(p)
            continue
        if node.left:
            s.append((node.left, p + [node.left.val]))
        if node.right:
            s.append((node.right, p + [node.right.val]))
    return list(res)


a = TreeNode(10)
a.left = TreeNode(5)
a.right = TreeNode(12)
a.left.left = TreeNode(4)
a.left.right = TreeNode(7)


print(FindPath(a,22))·

