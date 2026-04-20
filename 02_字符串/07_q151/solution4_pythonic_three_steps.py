class Solution:
    def reverseWords(self, s: str) -> str:
        # 方法三的逻辑：1. 清理空格 -> 2. 整体反转 -> 3. 单词反转
        # 使用 Python 内置函数实现：
        
        # 1. 清理空格：split() 会拆分并处理掉多余空格，join 用单个空格重新连接
        s = " ".join(s.split())
        
        # 2. 整体反转字符串 (Python 字符串不支持原地翻转，使用切片产生新对象)
        s = s[::-1]
        
        # 3. 单词反转：再次利用 split() 拆分单词，对每个单词翻转后 join
        # 这里逻辑是：单词顺序已经对了，但每个单词内部是反的
        return " ".join(word[::-1] for word in s.split())

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
