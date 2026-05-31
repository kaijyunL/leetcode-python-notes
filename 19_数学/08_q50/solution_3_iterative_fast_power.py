# 方法3：迭代快速幂 / 二进制拆指数（面试主推）
# base 每轮平方，指数每轮右移；当前二进制位是 1 时把 base 乘进答案
# 时间 O(log |n|)，空间 O(1)


class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1.0 / x
            n = -n

        ans = 1.0
        base = x

        while n > 0:
            if n & 1:
                ans *= base

            base *= base
            n >>= 1

        return ans


if __name__ == "__main__":
    solver = Solution()

    test_cases = [
        (2.0, 10, 1024.0),
        (2.1, 3, 9.261),
        (2.0, -2, 0.25),
        (1.0, -2147483648, 1.0),
        (-2.0, 3, -8.0),
        (-2.0, 4, 16.0),
        (5.0, 0, 1.0),
    ]

    for x, n, expected in test_cases:
        assert abs(solver.myPow(x, n) - expected) < 1e-9

    print("all tests passed")
