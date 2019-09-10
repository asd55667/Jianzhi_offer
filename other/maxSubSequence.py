# 最长严格上升子序列

def subSquence(s):
    mx = 0
    cache = [1] * len(s)
    for i in range(len(s)):
        for j in range(i):
            if s[i] > s[j]:
                dp[i] = max(dp[i], dp[j] + 1)
        mx = max(dp[i], mx)
    return mx

