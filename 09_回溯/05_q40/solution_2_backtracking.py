class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        """
        解法2：回溯 + 同层去重
        时间复杂度: 指数级
        空间复杂度: 指数级
        """
        candidates.sort()
        ans = []
        path = []

        def backtrack(start: int, remain: int) -> None:
            if remain == 0:
                ans.append(path[:])
                return

            if remain < 0:
                return

            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                num = candidates[i]
                path.append(num)
                backtrack(i + 1, remain - num)
                path.pop()

        backtrack(0, target)
        return ans


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        ([10, 1, 2, 7, 6, 1, 5], 8),
        ([2, 5, 2, 1, 2], 5),
        ([1, 1, 1, 6], 8),
    ]

    for candidates, target in test_cases:
        print(
            f"输入: candidates={candidates}, target={target}, "
            f"输出: {solution.combinationSum2(candidates, target)}"
        )
