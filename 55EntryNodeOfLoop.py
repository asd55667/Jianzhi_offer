class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def EntryNodeOfLoop(p):
    slow, fast = p, p 
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            # 起点到入口a, 入口到相遇点b
            # fast从相遇点绕环k圈回到b处，走了a+b(2倍率)
            # 从b倒回到a点，a =  k-1圈 + b到a点的距离
            cur = p
            while cur != slow:
                slow = slow.next
                cur = cur.next
            return cur    