# 方法1：排序后查缺口


class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        nums.sort()

        for i, num in enumerate(nums):
            if num != i:
                return i

        return len(nums)


if __name__ == "__main__":
    solver = Solution()
    test_cases = [
        [3, 0, 1],
        [0, 1],
        [9, 6, 4, 2, 3, 5, 7, 0, 1],
        [0],
    ]

    for nums in test_cases:
        print(f"nums={nums}, answer={solver.missingNumber(nums[:])}")
