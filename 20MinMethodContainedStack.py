


# two stack
class Solution:
    s = []
    m = [0x7fffffff]
    def push(self, node):
        self.s.append(node)
        if node < self.m[-1]:
            self.m.append(node)
        else: self.m.append(self.m[-1])


        # write code here
    def pop(self):
        # write code here
        self.m.pop()
        self.s.pop()
        
    def top(self):
        # write code here
        return self.s[-1] 

    def min(self):
        # write code here
        return self.m[-1]


class Solution:
    s = []
    m = 0x7fffffff
    def push(self, node):
        if node <= self.m:
            self.s.append(self.m)
        self.s.append(node)

        # write code here
    def pop(self):
        # write code here
        if self.s.pop() == self.m:
            self.m = self.s.pop()
            
    def top(self):
        # write code here
        return self.s[-1] 

    def min(self):
        # write code here
        return self.m

