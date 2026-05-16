from typing import List


# 方法二：记忆化递归
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)
        n = len(s)
        memo = {}

        def dfs(i):
            if i == n:
                return True
            if i in memo:
                return memo[i]

            for j in range(i + 1, n + 1):
                if s[i:j] in word_set and dfs(j):
                    memo[i] = True
                    return True

            memo[i] = False
            return False

        return dfs(0)


if __name__ == "__main__":
    solver = Solution()
    test_cases = [
        ("leetcode", ["leet", "code"]),
        ("applepenapple", ["apple", "pen"]),
        ("catsandog", ["cats", "dog", "sand", "and", "cat"]),
        ("cars", ["car", "ca", "rs"]),
    ]

    for s, word_dict in test_cases:
        print(f"s={s}, wordDict={word_dict}, answer={solver.wordBreak(s, word_dict)}")
