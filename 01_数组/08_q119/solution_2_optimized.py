def getRow(rowIndex: int):
    """
    方法二：空间优化 (滚动数组/原地更新)
    时间复杂度: O(n^2)
    空间复杂度: O(n) - 只使用一个数组存储结果
    """
    # 初始化一个全为 1 的数组，长度为 rowIndex + 1
    res = [1] * (rowIndex + 1)
    
    # 从第 2 行开始计算 (索引为 2)
    for i in range(2, rowIndex + 1):
        # 核心技巧：从后往前更新，避免覆盖上一行的旧值
        # 也就是计算第 i 行时，我们只改动索引 1 到 i-1 的值
        for j in range(i - 1, 0, -1):
            res[j] = res[j] + res[j-1]
            
    return res

# 测试代码
if __name__ == "__main__":
    test_rows = [0, 1, 3, 4]
    for r in test_rows:
        print(f"Index {r}: {getRow(r)}")
