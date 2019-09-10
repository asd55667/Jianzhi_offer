

def hasPath(matrix, rows, cols, path):
    def search(matrix,rows, cols, i, j, path, k, flag):
        idx = i*cols + j
        if i < 0 or i >= rows: return 0
        if j < 0 or j >= cols: return 0
        if matrix[idx] != path[k]: return 0
        if flag[idx]: return 0

        if k == len(path) - 1: return 1

        flag[idx] = 1
        if search(matrix, rows, cols, i-1, j, path, k+1, flag) or \
            search(matrix, rows, cols, i+1, j, path, k+1, flag) or \
                search(matrix, rows, cols, i, j-1, path, k+1, flag) or \
                    search(matrix, rows, cols, i, j+1, path, k+1, flag):
            return 1
        flag[idx] = 0
        return 0

    # matrix = [list(matrix[i*cols:(i+1)*cols]) for i in range(rows)]
    flag = [0]*len(matrix)
    for i in range(rows):
        for j in range(cols):
            if search(matrix,rows,cols, i,j, path, 0, flag):
                return 1
    return 0
            
print(hasPath('abcesfcsadee', 3,4,"bcced"))    #"abcb"