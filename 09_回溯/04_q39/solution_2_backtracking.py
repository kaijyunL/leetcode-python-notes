class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        """
        解法2：标准回溯
        时间复杂度: 指数级
        空间复杂度: 指数级
        """
        ans = []
        path = []

        def backtrack(start: int, remain: int) -> None:
            if remain == 0:
                ans.append(path[:])
                return

            if remain < 0:
                return

            for i in range(start, len(candidates)):
                num = candidates[i]
                path.append(num)
                backtrack(i, remain - num)
                path.pop()

        backtrack(0, target)
        return ans


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        ([2, 3, 6, 7], 7),
        ([2, 3, 5], 8),
        ([2], 1),
    ]

    for candidates, target in test_cases:
        print(
            f"输入: candidates={candidates}, target={target}, "
            f"输出: {solution.combinationSum(candidates, target)}"
        )
