
def NumberOf1Between1AndN_Solution(n):
    def h(n):
        c = 0
        while n:
            n, j = divmod(n,10)
            if j == 1:
                c += 1
        return c
    c = 0
    for i in range(1, n+1):
        c += h(i)
    return c

print(NumberOf1Between1AndN_Solution(13))