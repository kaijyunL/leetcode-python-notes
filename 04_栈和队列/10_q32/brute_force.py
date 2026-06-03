def longestValidParentheses(s: str) -> int:
    """
    暴力解法：检查所有偶数长度的子串
    时间复杂度: O(n^3)
    空间复杂度: O(n)
    """
    def isValid(sub: str) -> bool:
        stack = []
        for char in sub:
            if char == '(':
                stack.append('(')
            elif stack:
                stack.pop()
            else:
                return False
        return not stack

    n = len(s)
    max_len = 0
    # 遍历所有可能的子串
    for i in range(n):
        for j in range(i + 2, n + 1, 2):  # 步长为2，只检查偶数长度
            if isValid(s[i:j]):
                max_len = max(max_len, j - i)
    return max_len

if __name__ == "__main__":
    test_cases = ["(()", ")()())", "", "()(())"]
    for s in test_cases:
        print(f"Input: '{s}', Result: {longestValidParentheses(s)}")
