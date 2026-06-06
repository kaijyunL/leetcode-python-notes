# 方法1：每次只轮转一位

from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n

        for _ in range(k):
            previous = nums[-1]
            for i in range(n):
                nums[i], previous = previous, nums[i]


if __name__ == "__main__":
    solution = Solution()

    def check(nums, k, expected):
        solution.rotate(nums, k)
        assert nums == expected

    check([1, 2, 3, 4, 5, 6, 7], 3, [5, 6, 7, 1, 2, 3, 4])
    check([-1, -100, 3, 99], 2, [3, 99, -1, -100])
    check([1, 2], 3, [2, 1])
    check([1], 0, [1])

    print("all tests passed")
