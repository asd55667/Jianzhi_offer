class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


def Clone(pHead):        
    if not pHead: return None
    head = RandomListNode(pHead.label)
    tmp = head
    cur = pHead
    while cur.next:
        n = RandomListNode(cur.next.label)
        tmp.next = n
        if cur.random:
            n = RandomListNode(cur.random.label)
            tmp.random = n
        cur = cur.next
        tmp = tmp.next
    return head