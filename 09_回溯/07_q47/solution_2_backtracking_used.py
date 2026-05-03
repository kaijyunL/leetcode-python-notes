class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        """
        解法2：回溯 + used + 同层去重 — 面试推荐
        时间复杂度: O(n * n!)
        空间复杂度: O(n * n!)
        """
        nums.sort()
        ans = []
        path = []
        used = [False] * len(nums)

        def backtrack() -> None:
            if len(path) == len(nums):
                ans.append(path[:])
                return


            for i in range(len(nums)):
                if used[i]:
                    continue

                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue

                path.append(nums[i])
                used[i] = True
                backtrack()
                used[i] = False
                path.pop()

        backtrack()
        return ans


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        [1, 1, 2],
        [1, 2, 3],
        [1],
    ]

    for nums in test_cases:
        print(f"输入: nums={nums}, 输出: {solution.permuteUnique(nums)}")
