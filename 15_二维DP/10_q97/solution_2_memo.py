# 方法二：记忆化搜索
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        m, n = len(s1), len(s2)
        memo = {}

        def dfs(i, j):
            if i == m and j == n:
                return True
            if (i, j) in memo:
                return memo[(i, j)]

            k = i + j
            if i < m and s1[i] == s3[k] and dfs(i + 1, j):
                memo[(i, j)] = True
                return True
            if j < n and s2[j] == s3[k] and dfs(i, j + 1):
                memo[(i, j)] = True
                return True

            memo[(i, j)] = False
            return False

        return dfs(0, 0)


if __name__ == "__main__":
    solver = Solution()
    test_cases = [
        ("aabcc", "dbbca", "aadbbcbcac"),
        ("aabcc", "dbbca", "aadbbbaccc"),
        ("", "", ""),
        ("abc", "def", "adbcef"),
    ]

    for s1, s2, s3 in test_cases:
        print(f"s1={s1}, s2={s2}, s3={s3}, can={solver.isInterleave(s1, s2, s3)}")
