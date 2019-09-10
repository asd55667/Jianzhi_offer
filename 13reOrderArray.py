# No None Input

# Space O(n)  Time O(n)
def reOrderArray(array):
    s = [None] * len(array)
    l, r = 0, 0
    for n in array:
        if n % 2 != 0:
            r += 1
    for n in array:
        if n % 2 == 0:
            s[r] = n
            r += 1
        else:
            s[l] = n
            l += 1
    return s



# Space O(1) Time O(n^2)
def reOrderArray(array):
    n = len(array)
    i = 0
    while i < n:
        # skip odd
        while i < n and array[i] % 2 != 0:
            i += 1
        # skip even
        odd = i 
        while odd < n and array[odd] % 2 == 0:
            odd += 1
        # second time to meet odd
        # insert
        if odd < n:
            tmp = array[odd]
            for j in reversed(range(i, odd)):
                array[j+1] = array[j]
            array[i] = tmp
        i += 1
    return array

a = [3,4,8,7,2,1,5]
