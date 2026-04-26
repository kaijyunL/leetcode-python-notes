class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        """
        线性扫描：找到第一个下降点
        时间复杂度: O(n)
        空间复杂度: O(1)
        """
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                return i

        return len(nums) - 1


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        [1, 2, 3, 1],
        [1, 2, 1, 3, 5, 6, 4],
        [1],
        [2, 1],
        [1, 2],
    ]

    for nums in test_cases:
        print(f"nums = {nums}, result = {solution.findPeakElement(nums)}")
