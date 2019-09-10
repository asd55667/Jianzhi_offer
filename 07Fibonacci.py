
def Fibonacci(n):
    if n <= 1: return n
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)


def Fibonacci(n):
    def f(n, a, b):
        if n==0:return 0
        elif n == 1: return b
        else: return f(n-1, b, a+b)

    return f(n, 0, 1)


def Fibonacci(n):
    a, b = 0, 1
    while n:
        n -= 1
        b += a
        a = b - a 
    return a

def Fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b  = a, b + a 
    return a
    # 动态规划三个条件：最优子结构、无后效性、子问题重叠