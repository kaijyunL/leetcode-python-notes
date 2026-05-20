# 方法一：暴力递归
class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)

        def dfs(i: int) -> int:
            if i == n:
                return 1
            if s[i] == '0':
                return 0

            ways = dfs(i + 1)

            if i + 1 < n and 10 <= int(s[i:i + 2]) <= 26:
                ways += dfs(i + 2)

            return ways

        return dfs(0)


if __name__ == "__main__":
    solver = Solution()
    test_cases = [
        "12",
        "226",
        "06",
        "10",
    ]

    for s in test_cases:
        print(f"s={s}, ways={solver.numDecodings(s)}")
