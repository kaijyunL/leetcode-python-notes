def addBinary(a: str, b: str) -> str:
    """
    方法一：利用 Python 内置函数进行进制转换和求和。
    """
    # 1. 将二进制字符串转换为十进制整数
    # int(str, 2) 表示将 str 视为 2 进制进行解析
    num1 = int(a, 2)
    num2 = int(b, 2)
    
    # 2. 相加
    total = num1 + num2
    
    # 3. 将结果转换回二进制字符串
    # bin() 返回格式为 '0b100'，所以用 [2:] 去掉开头的 '0b'
    return bin(total)[2:]

# --- 测试代码 ---
if __name__ == "__main__":
    a1, b1 = "11", "1"
    print(f"输入: a = {a1}, b = {b1}")
    print(f"输出: {addBinary(a1, b1)}")  # 预期输出: 100

    a2, b2 = "1010", "1011"
    print(f"输入: a = {a2}, b = {b2}")
    print(f"输出: {addBinary(a2, b2)}")  # 预期输出: 10101
