class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        """
        解法2：回溯 + 字符串拼接
        时间复杂度: O(n * Cn)
        空间复杂度: O(n * Cn)
        """
        ans = []

        def backtrack(path: str, left: int, right: int) -> None:
            if len(path) == 2 * n:
                ans.append(path)
                return

            if left < n:
                backtrack(path + "(", left + 1, right)

            if right < left:
                backtrack(path + ")", left, right + 1)

        backtrack("", 0, 0)
        return ans


if __name__ == "__main__":
    solution = Solution()

    test_cases = [1, 2, 3]

    for n in test_cases:
        print(f"输入: n={n}, 输出: {solution.generateParenthesis(n)}")
