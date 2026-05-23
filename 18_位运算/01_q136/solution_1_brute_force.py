# 方法1：暴力统计


class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        for num in nums:
            count = 0
            for other in nums:
                if other == num:
                    count += 1
            if count == 1:
                return num


if __name__ == "__main__":
    solver = Solution()
    test_cases = [
        [2, 2, 1],
        [4, 1, 2, 1, 2],
        [1],
        [-1, -1, -2],
    ]

    for nums in test_cases:
        print(f"nums={nums}, answer={solver.singleNumber(nums)}")
