# 方法三：动态规划
class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 0 if s[0] == '0' else 1

        for i in range(2, n + 1):
            if s[i - 1] != '0':
                dp[i] += dp[i - 1]

            two_digits = int(s[i - 2:i])
            if 10 <= two_digits <= 26:
                dp[i] += dp[i - 2]

        return dp[n]


if __name__ == "__main__":
    solver = Solution()
    test_cases = [
        "12",
        "226",
        "06",
        "10",
    ]

    for s in test_cases:
        print(f"s={s}, ways={solver.numDecodings(s)}")
