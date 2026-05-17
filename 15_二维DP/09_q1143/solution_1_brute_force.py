# 方法一：暴力递归
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)

        def dfs(i, j):
            if i == m or j == n:
                return 0
            if text1[i] == text2[j]:
                return 1 + dfs(i + 1, j + 1)
            return max(dfs(i + 1, j), dfs(i, j + 1))

        return dfs(0, 0)


if __name__ == "__main__":
    solver = Solution()
    test_cases = [
        ("abcde", "ace"),
        ("abc", "abc"),
        ("abc", "def"),
        ("ezupkr", "ubmrapg"),
    ]

    for text1, text2 in test_cases:
        print(f"text1={text1}, text2={text2}, lcs={solver.longestCommonSubsequence(text1, text2)}")
