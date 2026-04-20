import functools

@functools.lru_cache(None)
def get_pascal_value(i, j):
    """
    计算杨辉三角第 i 行第 j 列的值 (i, j 从 0 开始)
    使用递归 + 装饰器缓存来避免重复计算导致的超时
    """
    # 边界情况：每一行的开头和结尾都是 1
    if j == 0 or j == i:
        return 1
    # 每个数是它左上方和右上方两数之和
    return get_pascal_value(i - 1, j - 1) + get_pascal_value(i - 1, j)

def generate_pascals_triangle_brute_force(numRows):
    """
    生成杨辉三角前 numRows 行
    """
    if numRows <= 0:
        return []
        
    triangle = []
    for i in range(numRows):
        row = []
        for j in range(i + 1):
            # 通过递归获取每一个位置的值
            value = get_pascal_value(i, j)
            row.append(value)
        triangle.append(row)
    return triangle

if __name__ == "__main__":
    # 测试输出
    rows = 26  # 现在即使设为 26 也不会超时了
    result = generate_pascals_triangle_brute_force(rows)
    print(f"杨辉三角前 {rows} 行（递归+缓存法）：")
    # 只打印最后一行展示结果
    print(f"第 {rows} 行结果：{result[-1]}")
