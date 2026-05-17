# 方法四：一维压缩动态规划
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = list(range(n + 1))

        for i in range(1, m + 1):
            prev_diagonal = dp[0]
            dp[0] = i

            for j in range(1, n + 1):
                current = dp[j]
                if word1[i - 1] == word2[j - 1]:
                    dp[j] = prev_diagonal
                else:
                    dp[j] = min(
                        dp[j],
                        dp[j - 1],
                        prev_diagonal,
                    ) + 1
                prev_diagonal = current

        return dp[n]


if __name__ == "__main__":
    solver = Solution()
    test_cases = [
        ("horse", "ros"),
        ("intention", "execution"),
        ("", "abc"),
        ("abc", "abc"),
    ]

    for word1, word2 in test_cases:
        print(f"word1={word1}, word2={word2}, distance={solver.minDistance(word1, word2)}")
