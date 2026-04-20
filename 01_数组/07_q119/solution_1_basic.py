def getRow(rowIndex: int):
    """
    方法一：基础动态规划 (生成所有行)
    时间复杂度: O(n^2)
    空间复杂度: O(n^2)
    """
    triangle = []
    
    for i in range(rowIndex + 1):
        # 当前行，长度为 i+1，首尾初始化为 1
        row = [1] * (i + 1)
        
        # 计算行中间的数字
        for j in range(1, i):
            # 每个数等于上一行左上方和正上方的数之和
            row[j] = triangle[i-1][j-1] + triangle[i-1][j]
        
        triangle.append(row)
    
    return triangle[rowIndex]

# 测试代码
if __name__ == "__main__":
    test_rows = [0, 1, 3, 4]
    for r in test_rows:
        print(f"Index {r}: {getRow(r)}")
