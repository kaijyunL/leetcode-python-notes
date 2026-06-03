def addBinary(a: str, b: str) -> str:
    """
    方法三：利用位运算 (Bit Manipulation) 实现在不使用 + 运算符的情况下求和。
    """
    # 先将字符串转换为整数
    x, y = int(a, 2), int(b, 2)
    
    while y:
        # 1. 计算无进位的加法结果 (使用 XOR)
        # 0^0=0, 1^1=0, 1^0=1, 0^1=1 (刚好符合二进制加法不计进位的逻辑)
        answer = x ^ y
        
        # 2. 计算进位 (使用 AND 并在左移一位)
        # 只有 1&1=1，且进位需要加在更高一位上，所以左移
        carry = (x & y) << 1
        
        # 3. 将结果赋值给 x, carry 赋值给 y，准备下一轮计算（直到进位为 0）
        x, y = answer, carry
        
    return bin(x)[2:]

# --- 测试代码 ---
if __name__ == "__main__":
    test_cases = [
        ("11", "1", "100"),
        ("1010", "1011", "10101")
    ]
    
    for a, b, expected in test_cases:
        result = addBinary(a, b)
        print(f"输入: a = {a}, b = {b}")
        print(f"输出: {result}, 预期: {expected}")
        assert result == expected
    print("\n所有测试用例通过！")
