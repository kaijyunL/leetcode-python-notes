# 方法1：暴力枚举

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n

        for i in range(n):
            product = 1
            for j in range(n):
                if i != j:
                    product *= nums[j]
            answer[i] = product

        return answer


if __name__ == "__main__":
    solution = Solution()

    assert solution.productExceptSelf([1, 2, 3, 4]) == [24, 12, 8, 6]
    assert solution.productExceptSelf([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]
    assert solution.productExceptSelf([2, 3]) == [3, 2]

    print("all tests passed")
