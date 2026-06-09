# 方法3：哈希集合

from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        seen = set()

        for num in nums:
            if num in seen:
                return num
            seen.add(num)

        return -1


if __name__ == "__main__":
    solution = Solution()

    assert solution.findDuplicate([1, 2, 3, 4, 2]) == 2
    assert solution.findDuplicate([3, 1, 3, 4, 2]) == 3
    assert solution.findDuplicate([1, 1]) == 1
    assert solution.findDuplicate([1, 1, 2]) == 1

    print("all tests passed")
