class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

'''链接：https://www.nowcoder.com/questionTerminal/9023a0c988684a53960365b889ceaf5e?f=discussion
来源：牛客网

1、有右子树的，那么下个结点就是右子树最左边的点；
2、没有右子树的，也可以分成两类，
    a)是父节点左孩子 ，那么父节点就是下一个节点 ； 
    b)是父节点的右孩子，找他的父节点的父节点的父节点...直到当前结点是其父节点的左孩子位置。如果没有eg：M，那么他就是尾节点。'''

def GetNext(p):
    if not p: return None
    # 1
    if p.right:
        p = p.right
        while p.left:
            p = p.left
        return p
    
    
    if p.next:
        # a
        if p.next.left == p:
            return p.next
        # b
        if p.next.right == p:
            while p.next.next:
                if p.next.next.left == p.next:
                    return p.next.next
                p = p.next
            return None
    return None

