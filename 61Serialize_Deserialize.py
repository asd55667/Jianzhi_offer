class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def Serialize(root):
    if not root: return ''
    que = [root]
    t = [root.val]
    while que:
        n = len(que)
        h_level = []
        for _ in range(n):
            node = que.pop(0)
            if not node.left and not node.right: break
            if node.left:
                que.append(node.left)
                h_level.append(node.left.val)
            else: 
                h_level.append('#')
            if node.right:
                que.append(node.right)
                h_level.append(node.right.val)
            else: 
                h_level.append('#')
        t += h_level
    t.append('!')
    t = map(str, t)
    return ','.join(t)


def Deserialize(s):
    if not s: return None
    s = s.split(',')
    root = TreeNode(int(s[0]))
    q = [root]
    i = 1
    while i < len(s)-1:
        node = q.pop(0)
        if s[i] == '!':
            break
        if s[i] == '#':
            node.left = None
        else:
            node.left = TreeNode(int(s[i]))
            q.append(node.left)
        if s[i+1] == '!':
            break
        if s[i+1] == '#':
            node.right = None
        else:
            node.right = TreeNode(int(s[i+1]))
            q.append(node.right)
        i += 2
    return root






# root = TreeNode(5)
# root.left = TreeNode(4)
# root.left.left = TreeNode(3)
# root.left.left.left = TreeNode(2)

root = TreeNode(8)
root.left = TreeNode(6)
root.right = TreeNode(10)
root.left.left = TreeNode(5)
root.left.right = TreeNode(7)
root.right.left = TreeNode(9)
root.right.right = TreeNode(11)

a = Serialize(root)
print(a)
b = Deserialize(a)
print(Serialize(b))

s = []
def dfs(root):
    if not root: return 
    s.append(root.val)
    dfs(root.left)
    dfs(root.right)

dfs(root)
print(s)




'''
链接：https://www.nowcoder.com/questionTerminal/cf7e25aa97c04cc1a68c8f040e71fb84?f=discussion
来源：牛客网

typedef TreeNode node;
typedef TreeNode* pnode;
typedef int* pint;
class Solution {
    vector<int> buf;
    void dfs(pnode p){
        if(!p) buf.push_back(0x23333);
        else{
            buf.push_back(p -> val);
            dfs(p -> left);
            dfs(p -> right);
        }
    }
    pnode dfs2(pint& p){
        if(*p == 0x23333){
            ++p;
            return NULL;
        }
        pnode res = new node(*p);
        ++p;
        res -> left = dfs2(p);
        res -> right = dfs2(p);
        return res;
    }
public:
    char* Serialize(TreeNode *p) {
        buf.clear();
        dfs(p);
        int *res = new int[buf.size()];
        for(unsigned int i = 0; i < buf.size(); ++i) res[i] = buf[i];
        return (char*)res;
    }
    TreeNode* Deserialize(char *str) {
        int *p = (int*)str;
        return dfs2(p);
    }
};

'''