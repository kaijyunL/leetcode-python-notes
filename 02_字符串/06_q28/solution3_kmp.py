#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def strStr(haystack: str, needle: str) -> int:
    """
    KMP 算法 (Knuth-Morris-Pratt)
    
    时间复杂度: O(n + m)
    空间复杂度: O(m)
    """
    if not needle:
        return 0
    
    m = len(needle)
    n = len(haystack)
    
    # 1. 预处理：构建 next 数组 (即 LPS: Longest Prefix which is also Suffix)
    # next[i] 表示 needle[0...i] 中最长的前后缀相同的长度
    next_arr = [0] * m
    j = 0 # j 指向前缀末尾，同时也表示当前最长相等前后缀长度
    for i in range(1, m): # i 指向后缀末尾
        # 如果当前字符不匹配，回退 j
        while j > 0 and needle[i] != needle[j]:
            j = next_arr[j - 1]
        
        # 如果当前字符匹配，j 向后移并记录长度
        if needle[i] == needle[j]:
            j += 1
        
        next_arr[i] = j
    
    # 2. 匹配过程
    j = 0 # j 代表当前 needle 已匹配到的位置
    for i in range(n): # i 代表当前 haystack 遍历到的位置
        # 如果当前字符不匹配，根据 next 数组回退 j
        while j > 0 and haystack[i] != needle[j]:
            j = next_arr[j - 1]
            
        # 如果当前字符匹配，j 继续向后
        if haystack[i] == needle[j]:
            j += 1
        
        # 如果 j 达到了 needle 的长度，说明完全匹配
        if j == m:
            return i - m + 1
            
    return -1

# 测试用例
if __name__ == "__main__":
    test_cases = [
        ("sadbutsad", "sad", 0),
        ("leetcode", "leeto", -1),
        ("hello", "ll", 2),
        ("aabaabaafa", "aabaaf", 3),
        ("a", "a", 0)
    ]
    
    for h, n, expected in test_cases:
        result = strStr(h, n)
        print(f"Haystack: '{h}', Needle: '{n}' -> Result: {result} (Expected: {expected})")
        assert result == expected
    
    print("\n所有 KMP 匹配测试用例通过！")
    print("Next Array Step-by-Step Example (for 'aabaaf'):")
    # 我们可以打印一下 next 数组来看看它的内部工作
    # a  a  b  a  a  f
    # 0  1  0  1  2  0
