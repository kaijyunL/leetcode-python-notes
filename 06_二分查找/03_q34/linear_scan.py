class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        """
        线性扫描：记录 target 的第一次和最后一次出现位置
        时间复杂度: O(n)
        空间复杂度: O(1)
        """
        start = -1
        end = -1

        for i, num in enumerate(nums):
            if num == target:
                if start == -1:
                    start = i
                end = i

        return [start, end]


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        ([5, 7, 7, 8, 8, 10], 8),
        ([5, 7, 7, 8, 8, 10], 6),
        ([], 0),
        ([1], 1),
    ]

    for nums, target in test_cases:
        print(f"nums = {nums}, target = {target}, result = {solution.searchRange(nums, target)}")
