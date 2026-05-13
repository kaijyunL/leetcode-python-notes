class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}

        def dfs(i: int) -> int:
            if i == 1:
                return 1
            if i == 2:
                return 2
            if i in memo:
                return memo[i]
            memo[i] = dfs(i - 1) + dfs(i - 2)
            return memo[i]

        return dfs(n)


if __name__ == "__main__":
    solver = Solution()
    for n in [1, 2, 3, 4, 5]:
        print(f"n={n}, ways={solver.climbStairs(n)}")
