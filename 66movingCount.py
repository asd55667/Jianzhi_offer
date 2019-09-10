

def movingCount(threshold, rows, cols):
        def numSum(n):
            s = 0
            while n:
                t = n % 10
                s += t
                n = n // 10
            return s
        
        def helper(i, j ,rows, cols, flag, threshold):
            if i < 0 or i >= rows: return 0
            if j < 0 or j >= cols: return 0
            if numSum(i) + numSum(j) > threshold: return 0
            if flag[i][j]: return 0
            flag[i][j] = 1
            return helper(i-1, j ,rows, cols, flag, threshold) + \
                    helper(i+1, j ,rows, cols, flag, threshold) + \
                    helper(i, j-1 ,rows, cols, flag, threshold) + \
                    helper(i, j+1 ,rows, cols, flag, threshold) + 1

        flag = [[0]*cols for _ in range(rows)]
        return helper(0,0, rows, cols, flag, threshold)


print(movingCount(10,1,100))
