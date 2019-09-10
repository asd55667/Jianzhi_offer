# 二维数组中的查找

def Find(target, array):
    # write code here
    m,n = len(array), len(array[0])
    i = 0
    while i < m and n > 0:
        if array[i][n-1] == target:
            return True
        elif array[i][n-1] < target:
            i += 1
        else: n -= 1
    return False