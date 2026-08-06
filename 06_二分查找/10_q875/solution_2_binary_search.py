# 方法2：二分答案（面试主推）


class Solution:
    def minEatingSpeed(self, piles, h):
        left = 1
        right = max(piles)

        while left <= right:
            mid = (left + right) // 2

            if self.can_finish(piles, h, mid):
                right = mid - 1
            else:
                left = mid + 1

        return left

    def can_finish(self, piles, h, speed):
        total_hours = 0

        for pile in piles:
            total_hours += (pile + speed - 1) // speed

        return total_hours <= h


if __name__ == "__main__":
    solution = Solution()

    assert solution.minEatingSpeed([3, 6, 7, 11], 8) == 4
    assert solution.minEatingSpeed([30, 11, 23, 4, 20], 5) == 30
    assert solution.minEatingSpeed([30, 11, 23, 4, 20], 6) == 23
    assert solution.minEatingSpeed([312884470], 312884469) == 2
    assert solution.minEatingSpeed([312884470], 312884470) == 1
    assert solution.minEatingSpeed([1, 1, 1, 1], 4) == 1
    assert solution.minEatingSpeed([9, 9, 9], 3) == 9
    assert solution.minEatingSpeed([805306368, 805306368, 805306368], 1000000000) == 3

    print("all tests passed")
