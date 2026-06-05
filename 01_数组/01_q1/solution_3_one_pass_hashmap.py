# 方法3：一遍哈希表（面试主推）

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pos = {}

        for i, num in enumerate(nums):
            need = target - num
            if need in pos:
                return [pos[need], i]
            pos[num] = i

        return []


if __name__ == "__main__":
    solution = Solution()

    assert solution.twoSum([2, 7, 11, 15], 9) == [0, 1]
    assert solution.twoSum([3, 2, 4], 6) == [1, 2]
    assert solution.twoSum([3, 3], 6) == [0, 1]
    assert solution.twoSum([-3, 4, 3, 90], 0) == [0, 2]

    print("all tests passed")
