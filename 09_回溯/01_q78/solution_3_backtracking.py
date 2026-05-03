class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        """
        解法3：回溯 — 面试推荐
        时间复杂度: O(n * 2^n)
        空间复杂度: O(n * 2^n)
        """
        ans = []
        path = []

        def backtrack(start: int) -> None:
            ans.append(path[:])

            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i + 1)
                path.pop()

        backtrack(0)
        return ans


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        [1, 2, 3],
        [0],
        [],
    ]

    for nums in test_cases:
        print(f"输入: nums={nums}, 输出: {solution.subsets(nums)}")
