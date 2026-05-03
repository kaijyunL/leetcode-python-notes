class Solution:
    def partition(self, s: str) -> list[list[str]]:
        """
        解法3：回溯 + 回文预处理 — 面试推荐
        时间复杂度: O(n * 2^n)
        空间复杂度: O(n * 2^n)
        """
        n = len(s)
        is_pal = [[False] * n for _ in range(n)]

        for left in range(n - 1, -1, -1):
            for right in range(left, n):
                if s[left] == s[right] and (
                    right - left <= 2 or is_pal[left + 1][right - 1]
                ):
                    is_pal[left][right] = True

        ans = []
        path = []

        def backtrack(start: int) -> None:
            if start == n:
                ans.append(path[:])
                return

            for end in range(start, n):
                if not is_pal[start][end]:
                    continue

                path.append(s[start:end + 1])
                backtrack(end + 1)
                path.pop()

        backtrack(0)
        return ans


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        "aab",
        "a",
        "efe",
        "aaa",
    ]

    for s in test_cases:
        print(f"输入: s={s!r}, 输出: {solution.partition(s)}")
