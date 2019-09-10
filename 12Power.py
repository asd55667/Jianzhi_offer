
def Power(base, exponent):
    res = 1.
    p = abs(exponent)
    while p:
        if p & 1:
            res *= base
        base *= base
        p >>= 1
    return res if exponent > 0 else 1/res 

