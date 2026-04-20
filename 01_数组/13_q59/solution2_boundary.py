# 方法二：边界收缩法
def generateMatrix2(n):
    # 初始化 n x n 的矩阵
    matrix = [[0] * n for _ in range(n)]
    
    # 初始化四个矩阵的边界参数
    # 左边界 和 右边界 控制列的起始和结束
    # 上边界 和 下边界 控制行的起始和结束
    left, right = 0, n - 1
    top, bottom = 0, n - 1
    
    # 这个变量用于记录我们要往矩阵中填的数字，初始为 1
    num = 1
    
    # target 就是 n^2，数字填满 n^2 时结束循环
    target = n * n
    
    while num <= target:
        # 1. 填最上面一层（只走没走过的列，范围：从左到右）
        for i in range(left, right + 1):
            matrix[top][i] = num
            num += 1
        # 最上面一层全填满了，所以把"上边界"往下移一步
        top += 1
        
        # 2. 填最右面一列（行范围：从上到下。注意此时最上面的一格已经在上一步被填过了，刚好 top+1 生效了）
        for i in range(top, bottom + 1):
            matrix[i][right] = num
            num += 1
        # 最右面一列全填满了，所以把"右边界"往左移一步
        right -= 1
        
        # 3. 填最下面一层（列范围：从右一直往左倒推）
        for i in range(right, left - 1, -1):
            matrix[bottom][i] = num
            num += 1
        # 最下方的一行全填满了，所以把"下边界"往上移一步
        bottom -= 1
        
        # 4. 填最左面一列（行范围：从下一直往上倒推）
        for i in range(bottom, top - 1, -1):
            matrix[i][left] = num
            num += 1
        # 最靠左边这一列全填满了，所以把"左边界"往右移一步
        left += 1
        
    return matrix

if __name__ == "__main__":
    n = 3
    print(f"n = {n} 的螺旋矩阵 (边界收缩法):")
    res = generateMatrix2(n)
    for r in res:
        print(r)
