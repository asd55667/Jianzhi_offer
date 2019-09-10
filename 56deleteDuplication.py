class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 去重 set
def deleteDuplication(p):
    if not p: return None
    cache = []
    cur, pre = p, None
    while cur:
        if cur.val in cache:
            pre.next = cur.next
            cur = cur.next
        else:
            cache.append(cur.val)
            pre = cur
            cur = cur.next
    return p

# 未排序 unique
def deleteDuplication(p):
    if not p: return None
    cache, dup = [], []
    cur = p
    while cur:
        if cur.val in cache:
            dup.append(cur.val)    
        else: cache.append(cur.val)
        cur = cur.next
    cur, pre, head = p, None, None
    while cur:
        if cur.val not in dup:
            if not pre:
                pre = cur
                head = pre
            else:
                pre.next = cur
                pre = cur
        cur = cur.next
    if pre:
        pre.next = None
    return head
    