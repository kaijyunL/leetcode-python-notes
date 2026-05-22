# 方法3：按右端点排序的贪心
class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        if len(intervals) <= 1:
            return 0

        intervals.sort(key=lambda item: item[1])
        keep_count = 1
        prev_end = intervals[0][1]

        for start, end in intervals[1:]:
            if start >= prev_end:
                keep_count += 1
                prev_end = end

        return len(intervals) - keep_count


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
