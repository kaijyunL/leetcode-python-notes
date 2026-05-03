class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        """
        解法1：暴力枚举 + set 去重
        时间复杂度: O(n * 2^n)
        空间复杂度: O(n * 2^n)
        """
        nums.sort()
        seen = set()
        n = len(nums)

        for mask in range(1 << n):
            subset = []
            for i in range(n):
                if mask & (1 << i):
                    subset.append(nums[i])
            seen.add(tuple(subset))

        return [list(subset) for subset in seen]


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        [1, 2, 2],
        [0],
        [1, 1, 1],
        [],
    ]

    for nums in test_cases:
        print(f"输入: nums={nums}, 输出: {solution.subsetsWithDup(nums)}")
