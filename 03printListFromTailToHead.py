#从尾到头打印链表
def printListFromTailToHead(listNode):
    # write code here
    res = []
    while listNode:
        res.append(listNode.val)
        listNode = listNode.next
    i, j = 0, len(res)-1
    while i < j:
        res[i], res[j] = res[j], res[i]
        i += 1
        j -= 1
    return res