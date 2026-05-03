class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        """
        解法1：位掩码枚举
        时间复杂度: O(n * 2^n)
        空间复杂度: O(n * 2^n)
        """
        n = len(nums)
        ans = []

        for mask in range(1 << n):
            subset = []
            for i in range(n):
                if mask & (1 << i):
                    subset.append(nums[i])
            ans.append(subset)

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
