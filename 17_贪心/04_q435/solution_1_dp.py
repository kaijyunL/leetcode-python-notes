# 方法1：DP
class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        if len(intervals) <= 1:
            return 0

        intervals.sort(key=lambda item: (item[0], item[1]))
        n = len(intervals)
        dp = [1] * n
        max_keep = 1

        for i in range(n):
            for j in range(i):
                if intervals[j][1] <= intervals[i][0]:
                    dp[i] = max(dp[i], dp[j] + 1)

            max_keep = max(max_keep, dp[i])

        return n - max_keep


if __name__ == "__main__":
    solver = Solution()
    test_cases = [
        [[1, 2], [2, 3], [3, 4], [1, 3]],
        [[1, 2], [1, 2], [1, 2]],
        [[1, 2], [2, 3]],
        [[1, 100], [11, 22], [1, 11], [2, 12]],
        [[-50, -20], [-10, 0], [-5, 10], [8, 15]],
    ]

    for intervals in test_cases:
        print(f"intervals={intervals}, removed={solver.eraseOverlapIntervals(intervals)}")
