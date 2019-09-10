
def duplicate(nums, dup):
    state = [False] * len(nums)
    for n in nums:
        if state[n]:
            dup[0] = n
            return True
        state[n] = True
    return False