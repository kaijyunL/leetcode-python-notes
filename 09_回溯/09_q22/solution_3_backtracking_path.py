class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        """
        解法3：回溯 + path 列表 — 面试推荐
        时间复杂度: O(n * Cn)
        空间复杂度: O(n * Cn)
        """
        ans = []
        path = []

        def backtrack(left: int, right: int) -> None:
            if len(path) == 2 * n:
                ans.append("".join(path))
                return

            if left < n:
                path.append("(")
                backtrack(left + 1, right)
                path.pop()

            if right < left:
                path.append(")")
                backtrack(left, right + 1)
                path.pop()

        backtrack(0, 0)
        return ans


if __name__ == "__main__":
    solution = Solution()

    test_cases = [1, 2, 3]

    for n in test_cases:
        print(f"输入: n={n}, 输出: {solution.generateParenthesis(n)}")
