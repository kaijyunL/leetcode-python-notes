# 方法3：栈存下标（面试主推）


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        """
        栈存下标：栈顶当合法子串的左边界参照点。
        时间复杂度: O(n)
        空间复杂度: O(n)
        """
        ans = 0
        stack = [-1]

        for i, ch in enumerate(s):
            if ch == "(":
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    ans = max(ans, i - stack[-1])

        return ans


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
