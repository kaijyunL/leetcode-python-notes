class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        """
        解法3：原地交换回溯
        时间复杂度: O(n * n!)
        空间复杂度: O(n * n!)
        """
        ans = []

        def backtrack(first: int) -> None:
            if first == len(nums):
                ans.append(nums[:])
                return

            for i in range(first, len(nums)):
                nums[first], nums[i] = nums[i], nums[first]
                backtrack(first + 1)
                nums[first], nums[i] = nums[i], nums[first]

        backtrack(0)
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
