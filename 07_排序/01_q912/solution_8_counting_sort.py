class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        """
        计数排序：统计每个数字出现次数后按顺序还原
        时间复杂度: O(n + k)
        空间复杂度: O(k)
        """
        if not nums:
            return nums

        min_num = min(nums)
        max_num = max(nums)
        counts = [0] * (max_num - min_num + 1)

        for num in nums:
            counts[num - min_num] += 1

        index = 0
        for offset, count in enumerate(counts):
            num = offset + min_num
            for _ in range(count):
                nums[index] = num
                index += 1

        return nums


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        [5, 2, 3, 1],
        [5, 1, 1, 2, 0, 0],
        [],
        [1],
        [-1, 5, 3, 4, 0],
        [2, 2, 2],
    ]

    for nums in test_cases:
        print(f"nums = {nums}, result = {solution.sortArray(nums[:])}")
