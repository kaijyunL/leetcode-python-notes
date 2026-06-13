# 方法三：哈希集合 + 只从起点出发

from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        ans = 0

        for num in num_set:
            if num - 1 in num_set:
                continue

            cur = num
            length = 1

            while cur + 1 in num_set:
                cur += 1
                length += 1

            ans = max(ans, length)

        return ans


if __name__ == "__main__":
    solution = Solution()

    assert solution.longestConsecutive([100, 4, 200, 1, 3, 2]) == 4
    assert solution.longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]) == 9
    assert solution.longestConsecutive([]) == 0
    assert solution.longestConsecutive([1, 2, 0, 1]) == 3

    print("all tests passed")
