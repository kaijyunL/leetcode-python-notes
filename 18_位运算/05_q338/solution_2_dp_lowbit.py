# 方法2：DP + 最低位


class Solution:
    def countBits(self, n: int) -> list[int]:
        ans = [0] * (n + 1)

        for i in range(1, n + 1):
            ans[i] = ans[i >> 1] + (i & 1)

        return ans


if __name__ == "__main__":
    solver = Solution()
    test_cases = [2, 5, 0, 8]

    for n in test_cases:
        print(f"n={n}, answer={solver.countBits(n)}")
