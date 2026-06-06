# 方法1：暴力前移

from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        size = len(nums)
        i = 0

        while i < size:
            if nums[i] == val:
                for j in range(i + 1, size):
                    nums[j - 1] = nums[j]
                size -= 1
                continue
            i += 1

        return size


if __name__ == "__main__":
    solution = Solution()

    def check(nums, val, expected_k, expected_remaining):
        k = solution.removeElement(nums, val)
        assert k == expected_k
        assert sorted(nums[:k]) == sorted(expected_remaining)
        assert all(num != val for num in nums[:k])

    check([3, 2, 2, 3], 3, 2, [2, 2])
    check([0, 1, 2, 2, 3, 0, 4, 2], 2, 5, [0, 1, 3, 0, 4])
    check([], 1, 0, [])
    check([1, 1, 1], 1, 0, [])
    check([4, 5], 3, 2, [4, 5])

    print("all tests passed")
