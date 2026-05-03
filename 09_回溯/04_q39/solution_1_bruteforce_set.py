class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        """
        解法1：暴力回溯 + set 去重
        时间复杂度: 指数级
        空间复杂度: 指数级
        """
        seen = set()
        path = []

        def backtrack(total: int) -> None:
            if total == target:
                seen.add(tuple(sorted(path)))
                return

            if total > target:
                return

            for num in candidates:
                path.append(num)
                backtrack(total + num)
                path.pop()

        backtrack(0)
        return [list(item) for item in seen]


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
