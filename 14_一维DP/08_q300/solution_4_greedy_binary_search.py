from bisect import bisect_left
from typing import List


# 方法四：贪心 + 二分查找
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        tails = []

        for num in nums:
            pos = bisect_left(tails, num)

            if pos == len(tails):
                tails.append(num)
            else:
                tails[pos] = num

        return len(tails)


if __name__ == "__main__":
    solver = Solution()
    test_cases = [
        [10, 9, 2, 5, 3, 7, 101, 18],
        [0, 1, 0, 3, 2, 3],
        [7, 7, 7, 7, 7, 7, 7],
        [4, 10, 4, 3, 8, 9],
    ]

    for nums in test_cases:
        print(f"nums={nums}, lis={solver.lengthOfLIS(nums)}")
