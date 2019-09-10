

def printMatrix(matrix):
    m, n = len(matrix), len(matrix[0])
    x1, x2 = 0, m
    y1, y2 = n, 0
    while x1 != x2:
        # first row
        for i in range(y2, y1):
            print(matrix[x1][i])
        x1 += 1
        # last column
        for i in range(x1, x2):
            print(matrix[i][y1-1])
        y1 -= 1
        # last row
        for i in reversed(range(y2, y1)):
            print(matrix[x2-1][i])
        x2 -= 1
        # first column
        for i in reversed(range(x1, x2)):
            print(matrix[i][y2])
        y2 += 1



def printMatrix(matrix):
    res = []
    while len(matrix):
        # __iadd__ faster than __extend__
        res += matrix.pop(0)    #    res.extend(matrix.pop(0))
        if matrix and matrix[0]:
            for row in matrix:
                res.append(row.pop())
        if matrix and matrix[0]:
            res += matrix.pop()[::-1] #  res.extend(matrix.pop()[::-1])
        if matrix and matrix[0]:
            for i in reversed(range(len(matrix))):
                res.append(matrix[i].pop(0))
    return res




'''
You can't use += for non-local variable (variable which is not local for function and also not global)

def main():
    l = [1, 2, 3]

    def foo():
        l.extend([4])

    def boo():
        l += [5]

    foo()
    print l
    boo()  # this will fail

main()
It's because for extend case compiler will load the variable l using LOAD_DEREF instruction, 

but for += it will use LOAD_FAST - and you get *UnboundLocalError: local variable 'l' referenced before assignment*
'''

import numpy as np  
a = [[1,2,3,4], [5,6,7,8],[9,10,11,12],[13,14,15,16]]

print(a)
print(printMatrix(a))


# 1 2 3 4  5 6 7 8  9 10 11 12  13 14 15 16 
# 1,2,3,4, 8,12,16, 15,14,13 ,9,5,6, 7,11,10.


