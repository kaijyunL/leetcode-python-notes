# 方法1：暴力计数

from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        threshold = len(nums) // 2

        for num in nums:
            count = 0
            for other in nums:
                if other == num:
                    count += 1
            if count > threshold:
                return num


if __name__ == "__main__":
    solution = Solution()

    assert solution.majorityElement([3, 2, 3]) == 3
    assert solution.majorityElement([2, 2, 1, 1, 1, 2, 2]) == 2
    assert solution.majorityElement([1]) == 1
    assert solution.majorityElement([6, 5, 5]) == 5

    print("all tests passed")
