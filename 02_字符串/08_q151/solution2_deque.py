from collections import deque

class Solution:
    def reverseWords(self, s: str) -> str:
        left, right = 0, len(s) - 1
        
        # 1. 去除首尾空格
        while left <= right and s[left] == ' ':
            left += 1
        while left <= right and s[right] == ' ':
            right -= 1
            
        dq, word = deque(), []
        
        # 2. 将单词逐个放入队列头部
        while left <= right:
            if s[left] == ' ' and word:
                # 遇到单词结束后的空格，将单词加入队列首部
                dq.appendleft("".join(word))
                word = []
            elif s[left] != ' ':
                # 正在读取单词
                word.append(s[left])
            left += 1
        
        # 别忘了最后一个单词
        dq.appendleft("".join(word))
        
        # 3. 合并字符串
        return " ".join(dq)

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
