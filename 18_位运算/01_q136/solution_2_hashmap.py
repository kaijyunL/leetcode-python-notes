# 方法2：哈希表计数


class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        counts = {}

        for num in nums:
            counts[num] = counts.get(num, 0) + 1

        for num in nums:
            if counts[num] == 1:
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
