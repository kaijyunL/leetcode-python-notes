def getRow(rowIndex: int):
    """
    方法三：数学公式法 (线性时间)
    利用组合数公式: C(n, k) = C(n, k-1) * (n - k + 1) / k
    时间复杂度: O(n)
    空间复杂度: O(n) - 存储结果数组
    """
    res = [1] * (rowIndex + 1)
    
    # 根据公式逐个计算
    # res[0] 已经是 1
    for i in range(1, rowIndex + 1):
        # res[i] = res[i-1] * (rowIndex - i + 1) / i
        # 注意 Python 的整数除法 //
        res[i] = res[i-1] * (rowIndex - i + 1) // i
        
    return res

# 测试代码
if __name__ == "__main__":
    test_rows = [0, 1, 3, 4]
    for r in test_rows:
        print(f"Index {r}: {getRow(r)}")
