# 方法1：生成所有排列后找下一个

import itertools
from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        n = len(nums)
        if n <= 1:
            return

        current = tuple(nums)
        all_permutations = sorted(set(itertools.permutations(sorted(nums))))
        current_index = all_permutations.index(current)
        next_index = (current_index + 1) % len(all_permutations)
        next_permutation = all_permutations[next_index]

        for index in range(n):
            nums[index] = next_permutation[index]


def run_case(nums, expected):
    actual = nums[:]
    Solution().nextPermutation(actual)
    assert actual == expected


if __name__ == "__main__":
    run_case([1, 2, 3], [1, 3, 2])
    run_case([3, 2, 1], [1, 2, 3])
    run_case([1, 1, 5], [1, 5, 1])
    run_case([1], [1])

    print("all tests passed")
