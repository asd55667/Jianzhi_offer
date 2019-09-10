# +100","5e2","-123","3.1416"和"-1E-16
def isNumeric(s):
    if not s: return 0
    if s[0] not in ['+', '-', '.'] and not s[0].isdigit(): return 0
        
    def allnum(s):
        if not s: return 0
        for c in s:
            if not c.isdigit():
                return 0
        return  1

    if s[0] in ['+', '-', '.']: 
        if s[1] in ['+', '-'] or len(s) == 1: return 0
        if s[1] == '.': s = s[2:]
        else: s = s[1:]
    if allnum(s): return 1

    if '.' in s:
        if len(s.split('.')) != 2: return 0
        a,b = s.split('.')
        if allnum(a) and isNumeric(b): return 1
        else: return 0
    
    for c in ['e', 'E']:
        if c in s:
            a,b = s.split(c)
            return isNumeric(a) and isNumeric(b)

print(isNumeric('1.2.3'))



'''
链接：https://www.nowcoder.com/questionTerminal/6f8c901d091949a5837e24bb82a731f2?f=discussion
来源：牛客网

class Solution {
public:
    bool isNumeric(char* str) {
        // 标记符号、小数点、e是否出现过
        bool sign = false, decimal = false, hasE = false;
        for (int i = 0; i < strlen(str); i++) {
            if (str[i] == 'e' || str[i] == 'E') {
                if (i == strlen(str)-1) return false; // e后面一定要接数字
                if (hasE) return false;  // 不能同时存在两个e
                hasE = true;
            } else if (str[i] == '+' || str[i] == '-') {
                // 第二次出现+-符号，则必须紧接在e之后
                if (sign && str[i-1] != 'e' && str[i-1] != 'E') return false;
                // 第一次出现+-符号，且不是在字符串开头，则也必须紧接在e之后
                if (!sign && i > 0 && str[i-1] != 'e' && str[i-1] != 'E') return false;
                sign = true;
            } else if (str[i] == '.') {
              // e后面不能接小数点，小数点不能出现两次
                if (hasE || decimal) return false;
                decimal = true;
            } else if (str[i] < '0' || str[i] > '9') // 不合法字符
                return false;
        }
        return true;
    }
};
'''