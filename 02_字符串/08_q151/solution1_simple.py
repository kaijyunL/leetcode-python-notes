class Solution:
    def reverseWords(self, s: str) -> str:
        # 1. 使用 split() 将字符串切分为单词列表
        # split() 会自动处理多余的空格（包括首尾空格和中间多个空格）
        words = s.split()
        
        # 2. 翻转列表中的单词顺序
        # [::-1] 是 Python 的切片翻转方法
        words = words[::-1]
        
        # 3. 将翻转后的列表用空格连接成字符串
        return " ".join(words)

# --- 测试代码 ---
if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        "the sky is blue",
        "  hello world  ",
        "a good   example"
    ]
    for test in test_cases:
        print(f"输入: '{test}' -> 输出: '{sol.reverseWords(test)}'")
