# 方法二：排序后线性扫描

from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        sorted_nums = sorted(nums)
        best = 1
        length = 1

        for i in range(1, len(sorted_nums)):
            if sorted_nums[i] == sorted_nums[i - 1]:
                continue

            if sorted_nums[i] == sorted_nums[i - 1] + 1:
                length += 1
            else:
                best = max(best, length)
                length = 1

        return max(best, length)


if __name__ == "__main__":
    solution = Solution()

    assert solution.longestConsecutive([100, 4, 200, 1, 3, 2]) == 4
    assert solution.longestConsecutive([0, 1, 1, 2]) == 3
    assert solution.longestConsecutive([]) == 0
    assert solution.longestConsecutive([7]) == 1

    print("all tests passed")
