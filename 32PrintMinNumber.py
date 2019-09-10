def PrintMinNumber(nums):
    from functools import cmp_to_key
    def cmp(n1, n2):
        a = str(n1)+str(n2)
        b = str(n2)+str(n1)
        if a == b: return 0
        if a > b: return 1
        if a < b: return -1
    res = ''
    nums = list(map(str, nums))
    nums.sort(key=cmp_to_key(cmp))
    
    return ''.join(nums).lstrip('0') or '0'


print(PrintMinNumber([3,32,321]))    