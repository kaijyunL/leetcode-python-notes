# 方法2：二分查找（面试主推）


class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x

        while left <= right:
            mid = (left + right) // 2
            square = mid * mid

            if square <= x:
                left = mid + 1
            else:
                right = mid - 1

        return right


if __name__ == "__main__":
    solution = Solution()

    assert solution.mySqrt(0) == 0
    assert solution.mySqrt(1) == 1
    assert solution.mySqrt(2) == 1
    assert solution.mySqrt(4) == 2
    assert solution.mySqrt(8) == 2
    assert solution.mySqrt(15) == 3
    assert solution.mySqrt(16) == 4
    assert solution.mySqrt(2147395599) == 46339

    print("all tests passed")
