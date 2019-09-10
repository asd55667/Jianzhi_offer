class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def Merge(pHead1, pHead2):
    if not pHead1: return pHead2
    if not pHead2: return pHead1
    if pHead1.val > pHead2.val:
        pHead = pHead2
        p = pHead1
    else: 
        pHead = pHead1
        p = pHead2
    cur = pHead
    while p:
        cur = insert(cur, p)
        p = p.next
    return pHead

def insert(pHead, node):
    cur = pHead
    while cur.val <= node.val:
        pre = cur
        cur = cur.next
    node.next = cur
    pre.next = node
    return cur

a = ListNode(1)
a.next = ListNode(2)
a.next.next = ListNode(8)
b = ListNode(3)

a = insert(a,b)
print(a.val, )#a.next.val, a.next.next.val, a.next.next.next.val)
    


def Merge(pHead1, pHead2):
    if not pHead1: return pHead2
    if not pHead2: return pHead1
    if pHead1.val < pHead2.val:
        pHead1.next = Merge(pHead1.next, pHead2)
        return pHead1
    else:
        pHead2.next = Merge(pHead1, pHead2.next)
        return pHead2



def Merge(pHead1, pHead2):
    if not pHead1: return pHead2
    if not pHead2: return pHead1
    res = None
    while pHead1 and pHead2:
        if pHead1.val < pHead2.val:
            if not res:
                res = cur = pHead1
            else:
                cur.next = pHead1
                cur = cur.next
            pHead1 = pHead1.next
        else:
            if not res:
                res = cur = pHead2
            else:
                cur.next = pHead2
                cur = cur.next
            pHead2 = pHead2.next
    if not pHead1:
        cur.next = pHead2
    else:
        cur.next = pHead1
    return res
        
                            
            
