
def NumberOf1(n):
    count = 0 
    # 符号位计数
    sign = 0
    if n < 0: sign = 1
    n &= 0x7fffffff
    while n: 
        n &= n - 1
        count += 1
    return count + sign 

