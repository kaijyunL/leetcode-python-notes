# 方法1：暴力连乘
# 按定义把 x 乘 abs(n) 次；负指数最后取倒数
# 时间 O(|n|)，空间 O(1)，大指数会超时


class Solution:
    def myPow(self, x: float, n: int) -> float:
        exp = abs(n)
        ans = 1.0

        for _ in range(exp):
            ans *= x

        if n < 0:
            return 1.0 / ans
        return ans


if __name__ == "__main__":
    solver = Solution()

    test_cases = [
        (2.0, 10, 1024.0),
        (2.1, 3, 9.261),
        (2.0, -2, 0.25),
        (1.0, -8, 1.0),
        (-2.0, 3, -8.0),
        (-2.0, 4, 16.0),
        (5.0, 0, 1.0),
    ]

    for x, n, expected in test_cases:
        assert abs(solver.myPow(x, n) - expected) < 1e-9

    print("all tests passed")
