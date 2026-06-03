def isPalindrome(s: str) -> bool:
    """
    解法二：双指针
    思路：在原字符串上使用首尾两个指针相向运动，跳过无效字符，实时进行比较。
    """
    left, right = 0, len(s) - 1
    
    while left < right:
        # 左指针跳过非字母数字字符
        while left < right and not s[left].isalnum():
            left += 1
        # 右指针跳过非字母数字字符
        while left < right and not s[right].isalnum():
            right -= 1
        
        # 此时 left 和 right 指向的都是有效字符，进行对比
        if s[left].lower() != s[right].lower():
            return False
        
        # 匹配成功，指针移动
        left += 1
        right -= 1
        
    return True

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
