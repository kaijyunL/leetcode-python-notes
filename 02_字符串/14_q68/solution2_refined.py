#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def fullJustify(words, maxWidth):
    """
    最适合面试的解法：精简模擬
    逻辑拆分为：1. 贪心分行 2. 填充空格
    """
    res = []
    i = 0
    n = len(words)
    
    while i < n:
        # 1. 确定当前行能放多少单词
        line_words = []
        line_len = 0
        while i < n and line_len + len(words[i]) + len(line_words) <= maxWidth:
            line_len += len(words[i])
            line_words.append(words[i])
            i += 1
        
        # 2. 格式化当前行
        num_words = len(line_words)
        
        # 情况A: 最后一行 或 只有一个单词 -> 左对齐
        if i == n or num_words == 1:
            line_str = " ".join(line_words)
            res.append(line_str.ljust(maxWidth))
        else:
            # 情况B: 普通行 -> 左右对齐
            total_spaces = maxWidth - line_len
            slots = num_words - 1
            avg_space = total_spaces // slots
            extra_space = total_spaces % slots
            
            # 使用列表推导式或循环构建
            parts = []
            for j in range(slots):
                parts.append(line_words[j])
                # 均匀分配基础空格 + 前 extra_space 个位置多补1个空格
                parts.append(" " * (avg_space + (1 if j < extra_space else 0)))
            parts.append(line_words[-1])
            res.append("".join(parts))
            
    return res

if __name__ == "__main__":
    # 测试样例
    test_cases = [
        (["What","must","be","shall","be."], 12),
        (["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], 20)
    ]
    
    for w, m in test_cases:
        print(f"\nmaxWidth: {m}")
        for line in fullJustify(w, m):
            print(f"'{line}'")
