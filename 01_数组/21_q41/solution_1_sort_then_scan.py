# 方法1：排序后从 1 开始扫描

from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        expected = 1

        for num in nums:
            if num < expected:
                continue
            if num == expected:
                expected += 1
                continue
            return expected

        return expected


def run_case(nums, expected):
    actual = Solution().firstMissingPositive(nums[:])
    assert actual == expected


if __name__ == "__main__":
    run_case([1, 2, 0], 3)
    run_case([3, 4, -1, 1], 2)
    run_case([7, 8, 9, 11, 12], 1)
    run_case([], 1)
    run_case([1, 1, 2, 2], 3)

    print("all tests passed")
