class Solution:
    def reverseWords(self, s: str) -> str:
        # 由于 Python 字符串不可变，首先转成字符列表
        l = list(s)
        
        # 第一阶段：手动去除多余空格 (双指针法)
        l = self.trim_spaces(l)
        
        # 第二阶段：翻转整个字符串
        self.reverse_range(l, 0, len(l) - 1)
        
        # 第三阶段：翻转每个单词
        self.reverse_each_word(l)
        
        return "".join(l)

    def trim_spaces(self, l: list) -> list:
        # 去除前导、尾随和中间多余空格
        n = len(l)
        left, right = 0, n - 1
        
        # 去首
        while left <= right and l[left] == ' ':
            left += 1
        # 去尾
        while left <= right and l[right] == ' ':
            right -= 1
            
        output = []
        while left <= right:
            if l[left] != ' ':
                output.append(l[left])
            elif output[-1] != ' ': # 只添加非连续空格
                output.append(l[left])
            left += 1
        return output

    def reverse_range(self, l: list, left: int, right: int) -> None:
        # 翻转指定范围内的列表元素
        while left < right:
            l[left], l[right] = l[right], l[left]
            left, right = left + 1, right - 1

    def reverse_each_word(self, l: list) -> None:
        # 逐个查找单词并翻转其内容
        n = len(l)
        start = end = 0
        
        while start < n:
            # 找到单词结尾
            while end < n and l[end] != ' ':
                end += 1
            # 翻转该单词
            self.reverse_range(l, start, end - 1)
            # 移动到下一个单词
            start = end + 1
            end += 1

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
