# 方法4：双计数器正反各扫一遍（空间最优）


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        """
        双计数器：正向反向各扫一遍，抓住两种断点。
        时间复杂度: O(n)
        空间复杂度: O(1)
        """
        def scan(chars: str, open_ch: str) -> int:
            left = right = best = 0
            for ch in chars:
                if ch == open_ch:
                    left += 1
                else:
                    right += 1
                if left == right:
                    best = max(best, 2 * right)
                elif right > left:
                    left = right = 0
            return best

        # 正向抓 ")" 过多；反向抓 "(" 过多
        return max(scan(s, "("), scan(reversed(s), ")"))


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
