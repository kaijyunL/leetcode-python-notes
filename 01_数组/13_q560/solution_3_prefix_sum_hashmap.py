# 方法三：前缀和 + 哈希表

from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans = 0
        current_sum = 0
        prefix_count = {0: 1}

        for num in nums:
            current_sum += num
            ans += prefix_count.get(current_sum - k, 0)
            prefix_count[current_sum] = prefix_count.get(current_sum, 0) + 1

        return ans


if __name__ == "__main__":
    solution = Solution()

    assert solution.subarraySum([1, 1, 1], 2) == 2
    assert solution.subarraySum([1, 2, 3], 3) == 2
    assert solution.subarraySum([1, -1, 0], 0) == 3
    assert solution.subarraySum([3], 3) == 1
    assert solution.subarraySum([1, 2, 1, 2, 1], 3) == 4

    print("all tests passed")
