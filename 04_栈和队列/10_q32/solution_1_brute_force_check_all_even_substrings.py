# 方法1：暴力枚举所有偶数子串


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        """
        暴力解法：枚举所有偶数长度子串，用栈验证合法性。
        时间复杂度: O(n^3)
        空间复杂度: O(n)
        """
        def is_valid(sub: str) -> bool:
            balance = 0
            for ch in sub:
                if ch == "(":
                    balance += 1
                elif balance:
                    balance -= 1
                else:
                    return False
            return balance == 0

        n = len(s)
        max_len = 0

        for i in range(n):
            for j in range(i + 2, n + 1, 2):
                if is_valid(s[i:j]):
                    max_len = max(max_len, j - i)

        return max_len


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
