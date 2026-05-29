# 方法1：直接算 n! 再数末尾 0
# 思路最直白但效率很差，n 一大就慢得不行（大整数乘法成本巨大）
# 仅用于对照、提醒自己题目本质不是 n!，而是 n! 里的因子 5


class Solution:
    def trailingZeroes(self, n: int) -> int:
        f = 1
        for i in range(1, n + 1):
            f *= i

        count = 0
        while f > 0 and f % 10 == 0:
            count += 1
            f //= 10
        return count


if __name__ == "__main__":
    s = Solution()
    print(s.trailingZeroes(0))    # 0
    print(s.trailingZeroes(3))    # 0
    print(s.trailingZeroes(5))    # 1
    print(s.trailingZeroes(10))   # 2
    print(s.trailingZeroes(30))   # 7
    print(s.trailingZeroes(100))  # 24
