def length_of_last_word(s: str) -> int:
    """
    方法一：内置函数分割法
    简单直观，适合快速实现。
    """
    # 1. 使用 split() 分割字符串
    # Python 的 split() 无参数时，会自动处理连续空格并忽略首尾空格
    words = s.split()
    
    # 2. 如果列表为空（即字符串全是空格），返回 0
    if not words:
        return 0
    
    # 3. 返回最后一个单词的长度
    return len(words[-1])

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
