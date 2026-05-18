# 方法2：记忆化搜索
class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        memo = {}

        def is_palindrome(left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        def dfs(start):
            if start == n:
                return 0
            if start in memo:
                return memo[start]

            best = float("inf")
            for end in range(start, n):
                if not is_palindrome(start, end):
                    continue
                best = min(best, 1 + dfs(end + 1))

            memo[start] = best
            return best

        return dfs(0) - 1


if __name__ == "__main__":
    solver = Solution()
    test_cases = [
        "aab",
        "a",
        "ab",
        "aabaa",
    ]

    for s in test_cases:
        print(f"s={s}, minCut={solver.minCut(s)}")
