# 方法3：左右指针 + 尾部覆盖

from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left = 0
        right = len(nums)

        while left < right:
            if nums[left] == val:
                nums[left] = nums[right - 1]
                right -= 1
            else:
                left += 1

        return left


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
