# 方法三：动态规划
class Solution:
    def numSquares(self, n: int) -> int:
        squares = []
        i = 1
        while i * i <= n:
            squares.append(i * i)
            i += 1

        dp = [0] + [n] * n

        for total in range(1, n + 1):
            for square in squares:
                if square > total:
                    break
                dp[total] = min(dp[total], dp[total - square] + 1)

        return dp[n]


if __name__ == "__main__":
    solver = Solution()
    for n in (1, 12, 13, 43):
        print(f"n={n}, count={solver.numSquares(n)}")
