
def Sum_Solution(n):
    def f(x):
        return 0xffffffff if x&1 else 0
    a, b, s = n, n+1, 0
    s += b & f(a); a >>= 1; b <<= 1
    s += b & f(a); a >>= 1; b <<= 1
    s += b & f(a); a >>= 1; b <<= 1
    s += b & f(a); a >>= 1; b <<= 1
    s += b & f(a); a >>= 1; b <<= 1
    s += b & f(a); a >>= 1; b <<= 1
    s += b & f(a); a >>= 1; b <<= 1
    s += b & f(a); a >>= 1; b <<= 1
        
    s += b & f(a); a >>= 1; b <<= 1
    s += b & f(a); a >>= 1; b <<= 1
    s += b & f(a); a >>= 1; b <<= 1
    s += b & f(a); a >>= 1; b <<= 1
    s += b & f(a); a >>= 1; b <<= 1
    s += b & f(a); a >>= 1; b <<= 1
    s += b & f(a); a >>= 1; b <<= 1
    s += b & f(a); a >>= 1; b <<= 1
        
    s += b & f(a); a >>= 1; b <<= 1
    s += b & f(a); a >>= 1; b <<= 1
    s += b & f(a); a >>= 1; b <<= 1
    s += b & f(a); a >>= 1; b <<= 1
    s += b & f(a); a >>= 1; b <<= 1
    s += b & f(a); a >>= 1; b <<= 1
    s += b & f(a); a >>= 1; b <<= 1
    s += b & f(a); a >>= 1; b <<= 1
        
    s += b & f(a); a >>= 1; b <<= 1
    s += b & f(a); a >>= 1; b <<= 1
    s += b & f(a); a >>= 1; b <<= 1
    s += b & f(a); a >>= 1; b <<= 1
    s += b & f(a); a >>= 1; b <<= 1
    s += b & f(a); a >>= 1; b <<= 1
    s += b & f(a); a >>= 1; b <<= 1
    s += b & f(a); a >>= 1; b <<= 1
    return s >> 1


print(Sum_Solution(100))

