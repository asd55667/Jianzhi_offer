#替换空格
def replaceSpace(s):
    # write code here
        count = 0
        for char in s:
            if char == ' ':
                count += 1
        res = [None] * (len(s) + count*2)
        for i in reversed(range(len(s))):
            if s[i] != ' ':
                res[i+count*2] = s[i]
            else:
                count -= 1
                res[i+count*2] = '%'
                res[i+count*2 + 1] = '2'
                res[i+count*2 + 2] = '0'
        return ''.join(res)

print(replaceSpace('We Are Happy'))
