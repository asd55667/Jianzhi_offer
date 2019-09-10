#用两个栈来实现一个队列
class Solution:
    s1 = []
    s2 = []
    def push(self, node):
        # write code here
        self.s1.append(node)

    def pop(self):
        # return xx
        if self.s2:
            
            return self.s2.pop()
        else:
            while self.s1:
                self.s2.append(self.s1.pop())
            return self.s2.pop()

