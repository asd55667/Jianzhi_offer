class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 返回ListNode
def ReverseList(pHead):
    if not pHead: return None
    cur = pHead
    pre = None
    while cur.next:
        tmp = cur.next
        cur.next = pre
        pre = cur
        cur = tmp
    cur.next = pre
    return cur


# Recursive 
# 1->2->3
#     <-
# 1->2->3
#     <-
# 1->2  3
#  <- <-
# 1->2  3
#  <- <-
# 1  2  3
def ReverseList(pHead):
    if not pHead or not pHead.next:
        return pHead
    p = ReverseList(pHead.next)
    pHead.next.next = pHead
    pHead.next = None
    return p


a = ListNode(1)
a.next = ListNode(2)
a.next.next = ListNode(3)

a = ReverseList(a)
print(a.val, a.next.val, a.next.next.val)
