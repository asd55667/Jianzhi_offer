
def multiply(A):
    if not A: return []
    B = [0]*len(A)
    def mul(nums):
        from functools import reduce
        return reduce(lambda x,y: x*y, nums)
    for i in range(len(A)):
        B[i] = mul(A[:i]+A[i+1:])
    return B
    
print(multiply([1,2,3,4,5]))