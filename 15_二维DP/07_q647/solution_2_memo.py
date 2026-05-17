# 方法二：记忆化递归
class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        memo = {}
        count = 0

        def dfs(left, right):
            if left >= right:
                return True
            if (left, right) in memo:
                return memo[(left, right)]
            if s[left] != s[right]:
                memo[(left, right)] = False
                return False

            memo[(left, right)] = dfs(left + 1, right - 1)
            return memo[(left, right)]

        for left in range(n):
            for right in range(left, n):
                if dfs(left, right):
                    count += 1

        return count


if __name__ == "__main__":
    solver = Solution()
    test_cases = [
        "abc",
        "aaa",
        "abba",
        "abac",
    ]

    for s in test_cases:
        print(f"s={s}, count={solver.countSubstrings(s)}")
