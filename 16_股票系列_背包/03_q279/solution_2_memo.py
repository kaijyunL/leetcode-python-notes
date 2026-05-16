# 方法二：记忆化递归
class Solution:
    def numSquares(self, n: int) -> int:
        squares = []
        i = 1
        while i * i <= n:
            squares.append(i * i)
            i += 1

        memo = {}

        def dfs(remain):
            if remain == 0:
                return 0
            if remain in memo:
                return memo[remain]

            best = remain
            for square in squares:
                if square > remain:
                    break
                best = min(best, dfs(remain - square) + 1)

            memo[remain] = best
            return best

        return dfs(n)


if __name__ == "__main__":
    solver = Solution()
    for n in (1, 12, 13, 43):
        print(f"n={n}, count={solver.numSquares(n)}")
