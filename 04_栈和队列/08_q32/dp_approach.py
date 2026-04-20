def longestValidParentheses(s: str) -> int:
    """
    动态规划解法
    dp[i] 表示以 s[i] 结尾的最长有效括号长度
    时间复杂度: O(n)
    空间复杂度: O(n)
    """
    n = len(s)
    if n == 0: return 0
    dp = [0] * n
    max_ans = 0
    
    for i in range(1, n):
        if s[i] == ')':
            # 情况1: 形如 ...()
            if s[i-1] == '(':
                dp[i] = (dp[i-2] if i >= 2 else 0) + 2
            # 情况2: 形如 ...)) 且前面有对应的 '('
            elif i - dp[i-1] > 0 and s[i - dp[i-1] - 1] == '(':
                # dp[i-1] 是内部长度，2 是当前匹配的一对，
                # dp[i - dp[i-1] - 2] 是这组括号之前的有效长度
                prev_len = dp[i - dp[i-1] - 2] if i - dp[i-1] >= 2 else 0
                dp[i] = dp[i-1] + 2 + prev_len
            max_ans = max(max_ans, dp[i])
            
    return max_ans

if __name__ == "__main__":
    test_cases = ["(()", ")()())", "", "()(())"]
    for s in test_cases:
        print(f"Input: '{s}', Result: {longestValidParentheses(s)}")
