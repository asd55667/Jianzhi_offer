
def rectCover(number):
    if number == 0: return 0
    a, b = 1, 2
    for _ in range(number-1):
        a,b = b, a+b
    return a