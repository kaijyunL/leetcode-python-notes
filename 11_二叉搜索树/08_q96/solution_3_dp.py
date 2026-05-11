class Solution:
    def numTrees(self, n: int) -> int:
        if n <= 1:
            return 1

        # dp[i] 表示 i 个节点能组成多少种 BST
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1

        for nodes in range(2, n + 1):
            for root in range(1, nodes + 1):
                dp[nodes] += dp[root - 1] * dp[nodes - root]

        return dp[n]


if __name__ == "__main__":
    solution = Solution()
    test_cases = [1, 2, 3, 4, 5]

    for n in test_cases:
        print(f"n = {n}, result = {solution.numTrees(n)}")
