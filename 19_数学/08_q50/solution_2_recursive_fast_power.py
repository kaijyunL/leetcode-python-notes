# 方法2：递归快速幂
# 利用 x^n = x^(n//2) * x^(n//2)，奇数指数再多乘一个 x
# 时间 O(log |n|)，空间 O(log |n|)


class Solution:
    def myPow(self, x: float, n: int) -> float:
        def fast_power(exp: int) -> float:
            if exp == 0:
                return 1.0

            half = fast_power(exp // 2)
            ans = half * half

            if exp % 2 == 1:
                ans *= x

            return ans

        ans = fast_power(abs(n))
        if n < 0:
            return 1.0 / ans
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
