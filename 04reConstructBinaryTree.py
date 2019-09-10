# 重建二叉树
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
# 返回构造的TreeNode根节点
def reConstructBinaryTree( pre, tin):
    # write code here
    if not tin:
        return None
    val = pre.pop(0)
    res = TreeNode(val)        
    for i in range(len(tin)):
        if tin[i] == val:
            l = tin[:i]
            r = tin[i+1:]
            break
    res.left = reConstructBinaryTree(pre[:len(l)],l)
    res.right = reConstructBinaryTree(pre[len(l):],r)
    return res

a = [1,2,4,7,3,5,6,8]
b = [4,7,2,1,5,3,8,6]
t = reConstructBinaryTree(a,b)

def pre(t):
    if t:
        print(t.val)
    if t.left:
        pre(t.left)
    if t.right:
        pre(t.right)


pre(t)
    



