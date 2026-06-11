# 方法2：用哈希集合检查 1, 2, 3 ...

from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        numbers = set(nums)
        n = len(nums)

        for target in range(1, n + 2):
            if target not in numbers:
                return target

        return n + 1


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
