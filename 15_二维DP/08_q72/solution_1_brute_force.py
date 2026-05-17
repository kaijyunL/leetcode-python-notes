# 方法一：暴力递归
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)

        def dfs(i, j):
            if i == m:
                return n - j
            if j == n:
                return m - i
            if word1[i] == word2[j]:
                return dfs(i + 1, j + 1)

            insert_cost = dfs(i, j + 1)
            delete_cost = dfs(i + 1, j)
            replace_cost = dfs(i + 1, j + 1)

            return min(insert_cost, delete_cost, replace_cost) + 1

        return dfs(0, 0)


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
