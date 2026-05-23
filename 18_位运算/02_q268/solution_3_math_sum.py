# 方法3：数学求和


class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)
        expected = n * (n + 1) // 2
        actual = sum(nums)
        return expected - actual


if __name__ == "__main__":
    solver = Solution()
    test_cases = [
        [3, 0, 1],
        [0, 1],
        [9, 6, 4, 2, 3, 5, 7, 0, 1],
        [0],
    ]

    for nums in test_cases:
        print(f"nums={nums}, answer={solver.missingNumber(nums)}")
