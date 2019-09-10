def FirstNotRepeatingChar(s):
    if not s: return -1
    from collections import defaultdict
    counter = defaultdict(int)
    for char in s:
        counter[char] += 1
    for i, char in enumerate(s):
        if counter[char] == 1:
            return i
    return -1


print(FirstNotRepeatingChar('aabv'))            