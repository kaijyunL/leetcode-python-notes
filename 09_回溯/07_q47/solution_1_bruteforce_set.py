class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        """
        解法1：暴力排列 + set 去重
        时间复杂度: O(n * n!)
        空间复杂度: O(n * n!)
        """
        seen = set()
        path = []
        used = [False] * len(nums)

        def backtrack() -> None:
            if len(path) == len(nums):
                seen.add(tuple(path))
                return

            for i in range(len(nums)):
                if used[i]:
                    continue

                path.append(nums[i])
                used[i] = True
                backtrack()
                used[i] = False
                path.pop()

        backtrack()
        return [list(item) for item in seen]


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        [1, 1, 2],
        [1, 2, 3],
        [1],
    ]

    for nums in test_cases:
        print(f"输入: nums={nums}, 输出: {solution.permuteUnique(nums)}")
