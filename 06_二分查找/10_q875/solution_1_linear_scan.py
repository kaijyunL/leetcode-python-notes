# 方法1：线性枚举速度


class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        max_speed = max(piles)

        for speed in range(1, max_speed + 1):
            total_hours = 0

            for pile in piles:
                total_hours += (pile + speed - 1) // speed

            if total_hours <= h:
                return speed

        return max_speed


if __name__ == "__main__":
    solution = Solution()

    assert solution.minEatingSpeed([3, 6, 7, 11], 8) == 4
    assert solution.minEatingSpeed([30, 11, 23, 4, 20], 5) == 30
    assert solution.minEatingSpeed([30, 11, 23, 4, 20], 6) == 23
    assert solution.minEatingSpeed([9], 9) == 1
    assert solution.minEatingSpeed([9], 5) == 2
    assert solution.minEatingSpeed([1, 1, 1, 1], 4) == 1
    assert solution.minEatingSpeed([9, 9, 9], 3) == 9

    print("all tests passed")
