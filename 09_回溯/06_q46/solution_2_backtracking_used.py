class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        """
        解法2：回溯 + used 数组 — 面试推荐
        时间复杂度: O(n * n!)
        空间复杂度: O(n * n!)
        """
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
        [1, 2, 3],
        [0, 1],
        [1],
    ]

    for nums in test_cases:
        print(f"输入: nums={nums}, 输出: {solution.permute(nums)}")
