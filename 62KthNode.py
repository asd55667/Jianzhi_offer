class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.s = []
    # 返回对应节点TreeNode
    def KthNode(self, pRoot, k):
        # write code here
        if k == 0: return None
        self.inOrder(pRoot)
        if k > len(self.s): return None
        return self.s[k-1]                
    def inOrder(self, root):
        if not root: return 
        self.inOrder(root.left)
        self.s.append(root)
        self.inOrder(root.right)




root = TreeNode(8)
root.left = TreeNode(6)
root.right = TreeNode(10)
root.left.left = TreeNode(5)
root.left.right = TreeNode(7)
root.right.left = TreeNode(9)
root.right.right = TreeNode(11)        



print(KthNode(root, 1))