from collections import deque

class Solution:
    def reverseWords(self, s: str) -> str:
        # 双端队列：从左到右扫描单词，每次插入队列头部，自然实现翻转
        left, right = 0, len(s) - 1

        # 去除首尾空格
        while left <= right and s[left] == ' ':
            left += 1
        while left <= right and s[right] == ' ':
            right -= 1

        dq = deque()
        word = []

        while left <= right:
            if s[left] != ' ':
                # 收集当前单词的字符
                word.append(s[left])
            elif word:
                # 遇到空格且 word 非空，说明一个单词结束了
                # appendleft：插入队列头部，后扫描到的单词反而排在前面
                dq.appendleft("".join(word))
                word = []
            # else: 连续空格，跳过
            left += 1

        # 别忘了最后一个单词（它后面没有空格来触发入队）
        dq.appendleft("".join(word))

        return " ".join(dq)


# --- 测试代码 ---
if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        "the sky is blue",
        "  hello world  ",
        "a good   example",
    ]
    for test in test_cases:
        print(f"输入: '{test}' -> 输出: '{sol.reverseWords(test)}'")
