class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 2

        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]


if __name__ == "__main__":
    solver = Solution()
    for n in [1, 2, 3, 4, 5]:
        print(f"n={n}, ways={solver.climbStairs(n)}")
