

# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


def Mirror(root):
    if not root: return None
    tmp = root.left
    root.left = root.right
    root.right = tmp
    if root.left:
        self.Mirror(root.left)
    if root.right:
        self.Mirror(root.right)
    return root