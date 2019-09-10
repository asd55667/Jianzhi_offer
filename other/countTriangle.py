# nxm grid  num of triangle grid point can form 

def countTriangle(n,m):
    def gcd(x, y):
        while y != 0:
            y = x % y
            x = y
        return x
    
    def c3x(x):
        return x * (x - 1) * (x - 2) / 6
    res = c3x((n+1)*(m+1)) - (m+1)*c3x(n+1) - (n+1)*c2x(m+1)
    for i in range(1, n+1):
        for j in range(1, m+1):
            res -= 2 * (gcd(i,j) - 1) * (m+1 - j) * (n+1 - j)
    return res

    