#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def strStr(haystack: str, needle: str) -> int:
    """
    暴力匹配解法 (Brute Force)
    
    外层遍历 haystack 的每个起始位置，
    内层检查连续的子串是否与 needle 相等。
    """
    n, m = len(haystack), len(needle)
    
    # 如果 needle 为空，按照 LeetCode 习惯通常返回 0
    if not needle:
        return 0
    
    # 遍历主串，只需遍历到能够容纳 needle 的最后一个起始位置
    for i in range(n - m + 1):
        # 截取子串并比较
        if haystack[i : i + m] == needle:
            return i
            
    return -1

# 测试用例
if __name__ == "__main__":
    test_cases = [
        ("sadbutsad", "sad", 0),
        ("leetcode", "leeto", -1),
        ("hello", "ll", 2),
        ("a", "a", 0)
    ]
    
    for h, n, expected in test_cases:
        result = strStr(h, n)
        print(f"Haystack: '{h}', Needle: '{n}' -> Result: {result} (Expected: {expected})")
        assert result == expected
    
    print("\n所有暴力匹配测试用例通过！")
