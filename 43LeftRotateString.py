
def LeftRotateString(s, n):
    if not s: return ''
    n %= len(s)
    s += s[:n]
    return s[n:]