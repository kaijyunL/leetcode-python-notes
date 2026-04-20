def length_of_last_word(s: str) -> int:
    """
    方法二：反向遍历法 (推荐面试使用)
    最优解：时间 O(N), 空间 O(1)
    """
    i = len(s) - 1
    
    # 1. 首先自后向前过滤掉末尾的所有空格
    # 直到遇到第一个非空格字符
    while i >= 0 and s[i] == ' ':
        i -= 1
        
    # 如果 i 变负数，说明整个字符串全是空格，没有单词
    if i < 0:
        return 0
        
    # 2. 从第一个非空格字符开始往回数，直到遇到下一个空格或到达字符串开头
    length = 0
    while i >= 0 and s[i] != ' ':
        length += 1
        i -= 1
        
    return length

# 测试代码
if __name__ == "__main__":
    test_cases = [
        "Hello World",
        "   fly me   to   the moon  ",
        "luffy is still joyboy",
        " ",
        "a"
    ]
    for text in test_cases:
        print(f"输入: '{text}' -> 长度: {length_of_last_word(text)}")
