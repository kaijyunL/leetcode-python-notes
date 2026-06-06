# 方法3：三次反转（面试主推）

from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n

        def reverse(left, right):
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        reverse(0, n - 1)
        reverse(0, k - 1)
        reverse(k, n - 1)


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
