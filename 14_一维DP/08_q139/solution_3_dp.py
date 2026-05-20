from typing import List


# 方法三：动态规划
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True

        for i in range(1, n + 1):
            for j in range(i):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break

        return dp[n]


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
