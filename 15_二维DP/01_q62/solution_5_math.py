# 方法五：组合数学
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        total = m + n - 2
        choose = min(m - 1, n - 1)
        answer = 1

        for i in range(1, choose + 1):
            answer = answer * (total - choose + i) // i

        return answer


if __name__ == "__main__":
    solver = Solution()
    test_cases = [
        (3, 7),
        (3, 2),
        (3, 3),
        (7, 3),
    ]

    for m, n in test_cases:
        print(f"m={m}, n={n}, paths={solver.uniquePaths(m, n)}")
