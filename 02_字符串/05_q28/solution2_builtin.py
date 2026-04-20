#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def strStr(haystack: str, needle: str) -> int:
    """
    使用 Python 内置方法 find()
    这是最实用、最推荐的工程实践方法。
    """
    return haystack.find(needle)

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
    
    print("\n所有内置函数测试用例通过！")
