class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        """
        方法1：位掩码枚举（理解选或不选）
        时间复杂度：O(n * 2^n)
        空间复杂度：O(n * 2^n)
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
        ([1, 2, 3], {(), (1,), (2,), (3,), (1, 2), (1, 3), (2, 3), (1, 2, 3)}),
        ([0], {(), (0,)}),
        ([], {()}),
    ]

    for nums, expected in test_cases:
        actual = {tuple(subset) for subset in solution.subsets(nums)}
        assert actual == expected

    print("all tests passed")
