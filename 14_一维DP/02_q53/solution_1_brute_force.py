class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        n = len(nums)
        best = nums[0]

        for i in range(n):
            for j in range(i, n):
                total = 0
                for k in range(i, j + 1):
                    total += nums[k]
                best = max(best, total)

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
