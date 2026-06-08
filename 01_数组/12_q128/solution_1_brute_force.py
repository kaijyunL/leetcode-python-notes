# 方法一：暴力枚举

from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        best = 1

        for num in nums:
            current = num
            length = 1

            while current + 1 in nums:
                current += 1
                length += 1

            best = max(best, length)

        return best


if __name__ == "__main__":
    solution = Solution()

    assert solution.longestConsecutive([100, 4, 200, 1, 3, 2]) == 4
    assert solution.longestConsecutive([0, 1, 1, 2]) == 3
    assert solution.longestConsecutive([]) == 0
    assert solution.longestConsecutive([7]) == 1

    print("all tests passed")
