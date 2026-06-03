#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def fullJustify(words, maxWidth):
    """
    基础模拟方法：按行处理，手动管理空格分配。
    """
    res = []
    curr_line = []
    curr_len = 0 # 当前行单词的总长度（不含空格）

    for w in words:
        # curr_len + len(curr_line) 是单词长度 + 单词间至少一个空格的长度
        if curr_len + len(w) + len(curr_line) <= maxWidth:
            curr_line.append(w)
            curr_len += len(w)
        else:
            # 处理当前行
            spaces_to_add = maxWidth - curr_len
            if len(curr_line) == 1:
                # 只有一个单词，左对齐
                res.append(curr_line[0] + ' ' * (maxWidth - len(curr_line[0])))
            else:
                # 多个单词，左右对齐
                slots = len(curr_line) - 1
                avg_space = spaces_to_add // slots
                extra_space = spaces_to_add % slots
                
                line_str = ""
                for i in range(slots):
                    line_str += curr_line[i]
                    line_str += ' ' * (avg_space + (1 if i < extra_space else 0))
                line_str += curr_line[-1]
                res.append(line_str)
            
            # 重置下一行
            curr_line = [w]
            curr_len = len(w)

    # 处理最后一行：左对齐，单词间一个空格，末尾补齐
    last_line = " ".join(curr_line)
    res.append(last_line + ' ' * (maxWidth - len(last_line)))
    
    return res

if __name__ == "__main__":
    # 测试样例
    words = ["This", "is", "an", "example", "of", "text", "justification."]
    maxWidth = 16
    result = fullJustify(words, maxWidth)
    for line in result:
        print(f"'{line}'")
