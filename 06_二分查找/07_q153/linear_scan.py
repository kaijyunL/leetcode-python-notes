class Solution:
    def findMin(self, nums: list[int]) -> int:
        """
        线性扫描：逐个比较找最小值
        时间复杂度: O(n)
        空间复杂度: O(1)
        """
        min_num = nums[0]

        for num in nums:
            if num < min_num:
                min_num = num

        return min_num


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        [3, 4, 5, 1, 2],
        [4, 5, 6, 7, 0, 1, 2],
        [11, 13, 15, 17],
        [1],
        [2, 1],
    ]

    for nums in test_cases:
        print(f"nums = {nums}, result = {solution.findMin(nums)}")
