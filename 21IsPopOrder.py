

def IsPopOrder(v1, v2):
    s = []
    pop = 0
    for v in v1:
        s.append(v)
        while s and s[-1] == v2[pos]:
            s.pop()
            pos += 1
    return False if s else True

