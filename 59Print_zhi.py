class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def Print(root):
    if not root: return []
    que = [root]
    t = []
    while que:
        n = len(que)
        h_level = []
        for _ in range(n):
            node = que.pop(0)
            h_level.append(node.val)
            if node.left:
                que.append(node.left)
            if node.right:
                que.append(node.right)
        t.append(h_level)    
    flag = 1
    res = []
    for row in t:
        if flag == -1:
            row.reverse()
        res.append(row)
        flag *= -1
    return res


root = TreeNode(8)
root.left = TreeNode(6)
root.right = TreeNode(9)
root.left.left = TreeNode(5)
root.left.right = TreeNode(7)
root.right.left = TreeNode(7)
root.right.right = TreeNode(5)
print(Print(root))