def isPalindrome(s: str) -> bool:
    """
    解法一：筛选后的字符串反转
    思路：通过列表推导式或循环提取所有数字字母，转小写后与反转后的字符串比较。
    """
    # 1. 筛选并转换：只保留字母和数字，并转成小写
    # isalnum() 方法用于判断字符是否是字母或数字
    filtered_chars = "".join(ch.lower() for ch in s if ch.isalnum())
    
    # 2. 比较：将处理后的字符串与其反转后的版本进行对比
    # [::-1] 是 Python 字符串/列表取反的快捷写法
    return filtered_chars == filtered_chars[::-1]

# 测试代码
if __name__ == "__main__":
    test_cases = [
        ("A man, a plan, a canal: Panama", True),
        ("race a car", False),
        (" ", True)
    ]
    
    for s, expected in test_cases:
        result = isPalindrome(s)
        print(f"输入: \"{s}\"")
        print(f"结果: {result}, 预期: {expected}")
        print("-" * 20)
