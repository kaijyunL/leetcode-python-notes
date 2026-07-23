# 方法1：线性扫描


class Solution:
    def mySqrt(self, x: int) -> int:
        i = 0

        while i * i <= x:
            i += 1

        return i - 1


if __name__ == "__main__":
    solution = Solution()

    assert solution.mySqrt(0) == 0
    assert solution.mySqrt(1) == 1
    assert solution.mySqrt(2) == 1
    assert solution.mySqrt(4) == 2
    assert solution.mySqrt(8) == 2
    assert solution.mySqrt(15) == 3
    assert solution.mySqrt(16) == 4

    print("all tests passed")
