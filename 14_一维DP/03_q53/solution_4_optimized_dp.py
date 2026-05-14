class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        curr = nums[0]
        best = nums[0]

        for num in nums[1:]:
            curr = max(curr + num, num)
            best = max(best, curr)

        return best


if __name__ == "__main__":
    solver = Solution()
    test_cases = [
        [-2, 1, -3, 4, -1, 2, 1, -5, 4],
        [1],
        [5, 4, -1, 7, 8],
        [-1, -2, -3],
    ]

    for nums in test_cases:
        print(f"nums={nums}, max_sum={solver.maxSubArray(nums)}")
