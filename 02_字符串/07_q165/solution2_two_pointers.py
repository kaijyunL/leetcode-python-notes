def compareVersion(version1: str, version2: str) -> int:
    """
    方法二：双指针法
    思路：直接在原字符串上移动，动态解析每个修订号，节省空间。
    """
    n1, n2 = len(version1), len(version2)
    i, j = 0, 0
    
    while i < n1 or j < n2:
        v1, v2 = 0, 0
        
        while i < n1 and version1[i] != '.':
            v1 = v1 * 10 + int(version1[i])
            i += 1
        i += 1
        
        while j < n2 and version2[j] != '.':
            v2 = v2 * 10 + int(version2[j])
            j += 1
        j += 1
        
        if v1 > v2:
            return 1
        if v1 < v2:
            return -1
            
    return 0

# 测试代码
if __name__ == "__main__":
    test_cases = [
        ("1.01", "1.001"),    # 期望: 0
        ("1.0", "1.0.0"),     # 期望: 0
        ("0.1", "1.1"),       # 期望: -1
        ("1.0.1", "1"),       # 期望: 1
    ]
    
    print("--- 方法二：双指针法 ---")
    for v1, v2 in test_cases:
        result = compareVersion(v1, v2)
        print(f"Compare '{v1}' and '{v2}': {result}")
