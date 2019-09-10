class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def FindKthToTail(head, k):

    length = 0
    cur = head
    while cur: 
        cur = cur.next
        length += 1
    if length < k: return None
    i = length - k 
    for _ in range(i):
        head = head.next
    return head


def FindKthToTail(head, k):

    cur = head
    i = 0
    while cur:
        cur = cur.next
        if i >= k:
            head = head.next
        i += 1
    return head if i >= k else None