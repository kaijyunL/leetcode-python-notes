class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        """
        解法1：暴力回溯 + set 去重
        时间复杂度: 指数级
        空间复杂度: 指数级
        """
        seen = set()
        path = []

        def backtrack(index: int, total: int) -> None:
            if total == target:
                seen.add(tuple(sorted(path)))
                return

            if index == len(candidates) or total > target:
                return

            path.append(candidates[index])
            backtrack(index + 1, total + candidates[index])
            path.pop()

            backtrack(index + 1, total)

        backtrack(0, 0)
        return [list(item) for item in seen]


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
