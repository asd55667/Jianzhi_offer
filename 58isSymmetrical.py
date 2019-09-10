class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def isSymmetrical(root):
    if not root: return 1
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
            else: que.append(TreeNode('#'))
            if node.right:
                que.append(node.right)
            else: que.append(TreeNode('#'))
        if len(set(h_level)) == 1 and '#' in set(h_level):
            break
        t.append(h_level)
    for row in t[1:]:
        if len(row) % 2 != 0:
            return 0
        l, r = 0, len(row) - 1
        while l < r:
            if row[l] == row[r]:
                r -= 1
                l += 1
            else:
                return 0
    return 1

def isSymmetrical(root):
    def compare(p1,p2):
        if not p1 and not p2: return 1
        if not p1 or not p2: return 0
        if p1.val == p2.val:
            if compare(p1.left, p2.right) and compare(p1.right, p2.left):
                return 1
        retur 0
    if not root: return 1
    return compare(root.left, root.right)


root = TreeNode(8)
root.left = TreeNode(6)
root.right = TreeNode(9)
root.left.left = TreeNode(5)
root.left.right = TreeNode(7)
root.right.left = TreeNode(7)
root.right.right = TreeNode(5)
print(isSymmetrical(root))