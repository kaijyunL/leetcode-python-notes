# 方法2：动态规划


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        """
        DP：dp[i] 是以 s[i] 结尾的最长有效括号长度。
        时间复杂度: O(n)
        空间复杂度: O(n)
        """
        n = len(s)
        if n == 0:
            return 0

        dp = [0] * n
        max_ans = 0

        for i in range(1, n):
            if s[i] != ")":
                continue

            # 情况一：...()
            if s[i - 1] == "(":
                dp[i] = (dp[i - 2] if i >= 2 else 0) + 2

            # 情况二：...))，跳过内部合法段找配对的 (
            elif i - dp[i - 1] > 0 and s[i - dp[i - 1] - 1] == "(":
                inner = dp[i - 1]
                j = i - inner - 1
                prev = dp[j - 1] if j >= 1 else 0
                dp[i] = inner + 2 + prev

            max_ans = max(max_ans, dp[i])

        return max_ans


def run_test() -> None:
    solver = Solution()
    test_cases = [
        ("(()", 2),
        (")()())", 4),
        ("", 0),
        ("()(())", 6),
        ("()(()", 2),
        ("(((((", 0),
        ("))))", 0),
        ("()()", 4),
        ("(()())", 6),
    ]

    for s, expected in test_cases:
        result = solver.longestValidParentheses(s)
        assert result == expected, (
            f"failed for {s!r}: expected {expected}, got {result}"
        )


if __name__ == "__main__":
    run_test()
    print("all tests passed")
