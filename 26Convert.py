class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def Convert(t):
    if not t: return None
    p = t
    pre = root = None
    head = 1
    s = []
    while s and p:
        while p:
            s.append(p)
            p = p.left
        p = s.pop()
        if head:
            root = p
            pre = root
            head = 0
        else:
            pre.right = p
            p.left = pre
            pre = p
        p = p.right
    return root

def Convert(t):  # !
    def helper(cur, pre):
        if not cur: return 
        helper(cur.left, pre)
        cur.left = pre
        if pre:
            pre.right = cur
        pre = cur
        helper(cur.right, pre)
        
    if not t: return
    helper(t.left, None)
    res = t
    while res.left:
        res = res.left
    return res




def Convert(root):
    if not root:
        return None
    if not root.left and not root.right:
        return root
        
    # 将左子树构建成双链表，返回链表头
    left = Convert(root.left)
    p = left
        
    # 定位至左子树的最右的一个结点
    while left and p.right:
        p = p.right
        
    # 如果左子树不为空，将当前root加到左子树链表
    if left:
        p.right = root
        root.left = p
        
    # 将右子树构造成双链表，返回链表头
    right = Convert(root.right)
    # 如果右子树不为空，将该链表追加到root结点之后
    if right:
        right.left = root
        root.right = right
            
    return left if left else root



a = TreeNode(6)
a.left = TreeNode(4)
a.right = TreeNode(8)

Convert(a)
print(a.left.val,a.val, a.right.val,)