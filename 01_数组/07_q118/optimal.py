def generate_pascals_triangle_optimal(numRows):
    """
    使用迭代法生成杨辉三角
    这是 LeetCode 官方推荐的最优解法
    时间复杂度: O(numRows^2)
    空间复杂度: O(numRows^2)
    """
    # 如果输入的行数为 0，返回空列表
    if numRows == 0:
        return []

    # 初始化杨辉三角，第一行总是 [1]
    triangle = [[1]]

    # 从第二行开始构建 (索引从 1 到 numRows-1)
    for i in range(1, numRows):
        # 获取上一行的引用
        prev_row = triangle[i - 1]
        
        # 当前行的第一个元素总是 1
        current_row = [1]
        
        # 填充中间的元素：每个数等于上一行左上方和右上方两数之和
        # 索引 j 从 1 遍历到 i-1
        for j in range(1, i):
            val = prev_row[j - 1] + prev_row[j]
            current_row.append(val)
            
        # 当前行的最后一个元素总是 1
        current_row.append(1)
        
        # 将当前行加入到三角形中
        triangle.append(current_row)
        
    return triangle

if __name__ == "__main__":
    # 测试输出
    rows = 5
    result = generate_pascals_triangle_optimal(rows)
    print(f"杨辉三角前 {rows} 行（迭代最优解）：")
    for r in result:
        # 为了美观，这里稍微排版一下输出
        print(f"{str(r):^20}")
