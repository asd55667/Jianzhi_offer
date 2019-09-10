

def jumpFloor(number):
    a, b = 1, 2
    for _ in range(number-1):
        a,b = b, a + b
    return a

# number 相当于是序列从0开始的索引,  类似generator
# [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987 ...]