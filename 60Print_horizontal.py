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
    return t