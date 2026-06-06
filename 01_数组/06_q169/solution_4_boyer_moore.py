# 方法4：摩尔投票法（面试主推）

from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = 0
        count = 0

        for num in nums:
            if count == 0:
                candidate = num
            if num == candidate:
                count += 1
            else:
                count -= 1

        return candidate


if __name__ == "__main__":
    solution = Solution()

    assert solution.majorityElement([3, 2, 3]) == 3
    assert solution.majorityElement([2, 2, 1, 1, 1, 2, 2]) == 2
    assert solution.majorityElement([1]) == 1
    assert solution.majorityElement([6, 5, 5]) == 5

    print("all tests passed")
