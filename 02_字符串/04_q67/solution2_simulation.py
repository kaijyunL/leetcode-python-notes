def addBinary(a: str, b: str) -> str:
    """
    方法二：字符串逐位模拟加法。
    模拟竖式加法的过程，从右向左依次相加，并处理进位。
    """
    res = []
    carry = 0  # 存储进位
    
    # 指针分别指向 a 和 b 的末尾
    i, j = len(a) - 1, len(b) - 1
    
    # 只要有一个字符串没遍历完，或者还有进位，就继续循环
    while i >= 0 or j >= 0 or carry:
        # 获取当前位的值，如果指针已经越界（字符串遍历完了），则取 0
        digit_a = int(a[i]) if i >= 0 else 0
        digit_b = int(b[j]) if j >= 0 else 0
        
        # 计算当前位的总和（包含进位）
        total = digit_a + digit_b + carry
        
        # 计算新的进位
        carry = total // 2
        
        # 计算当前位的结果数字，添加到结果列表中
        res.append(str(total % 2))
        
        # 指针向前移动
        i -= 1
        j -= 1
    
    # 因为我们是从低位到高位添加的，最后需要反转回来，并拼接成字符串
    return "".join(res[::-1])

# --- 测试代码 ---
if __name__ == "__main__":
    test_cases = [
        ("11", "1", "100"),
        ("1010", "1011", "10101"),
        ("0", "0", "0"),
        ("1", "111", "1000")
    ]
    
    for a, b, expected in test_cases:
        result = addBinary(a, b)
        print(f"输入: a = {a}, b = {b}")
        print(f"输出: {result}, 预期: {expected}")
        assert result == expected
    print("\n所有测试用例通过！")
