
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def FindFirstCommonNode(p1,p2):
    if not p1 or not p2: return None
    while p1:
        cur = p2
        while cur:
            if cur == p1: return cur
            else: cur = cur.next
        p1 = p1.next
    return None

a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
a.next = b
c.next = b
print(FindFirstCommonNode(a,b))
