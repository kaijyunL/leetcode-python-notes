def compareVersion(version1: str, version2: str) -> int:
    """
    方法一：分割字符串法
    思路：将版本号按 '.' 分割成列表，逐位比较。
    """
    # 1. 按 '.' 分割字符串，得到修订号列表
    nums1 = version1.split('.')
    nums2 = version2.split('.')
    
    n1, n2 = len(nums1), len(nums2)
    
    # 2. 遍历较长的那个列表
    for i in range(max(n1, n2)):
        # 3. 如果超出当前版本号长度，则视为 0
        # 同时利用 int() 自动处理前导零 (如 "001" -> 1)
        v1 = int(nums1[i]) if i < n1 else 0
        v2 = int(nums2[i]) if i < n2 else 0
        
        # 4. 逐位比较
        if v1 > v2:
            return 1
        if v1 < v2:
            return -1
            
    # 5. 全部相等返回 0
    return 0

# 测试代码
if __name__ == "__main__":
    test_cases = [
        ("1.01", "1.001"),    # 期望: 0
        ("1.0", "1.0.0"),     # 期望: 0
        ("0.1", "1.1"),       # 期望: -1
        ("1.0.1", "1"),       # 期望: 1
    ]
    
    print("--- 方法一：分割字符串法 ---")
    for v1, v2 in test_cases:
        result = compareVersion(v1, v2)
        print(f"Compare '{v1}' and '{v2}': {result}")
