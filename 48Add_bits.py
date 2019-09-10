

def Add(n1, n2):
    # 防溢出
    mask = 0xffffffff
    while n2:
        n1, n2 = (n1^n2)& mask, ((n1&n2)<<1)&mask
    return n1 if n1<=0x7ffffff else ~(n1^mask)
    
print(Add(100,150))