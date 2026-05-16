# 方法一：暴力递归
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def dfs(row, col):
            if row == m - 1 and col == n - 1:
                return 1

            ways = 0

            if row + 1 < m:
                ways += dfs(row + 1, col)
            if col + 1 < n:
                ways += dfs(row, col + 1)

            return ways

        return dfs(0, 0)


if __name__ == "__main__":
    solver = Solution()
    test_cases = [
        (3, 7),
        (3, 2),
        (3, 3),
    ]

    for m, n in test_cases:
        print(f"m={m}, n={n}, paths={solver.uniquePaths(m, n)}")
