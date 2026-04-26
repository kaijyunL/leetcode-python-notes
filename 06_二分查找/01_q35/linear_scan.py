class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        """
        线性扫描：找到第一个大于等于 target 的位置
        时间复杂度: O(n)
        空间复杂度: O(1)
        """
        for i, num in enumerate(nums):
            if num >= target:
                return i

        return len(nums)


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        ([1, 3, 5, 6], 5),
        ([1, 3, 5, 6], 2),
        ([1, 3, 5, 6], 7),
        ([1, 3, 5, 6], 0),
    ]

    for nums, target in test_cases:
        print(f"nums = {nums}, target = {target}, result = {solution.searchInsert(nums, target)}")
