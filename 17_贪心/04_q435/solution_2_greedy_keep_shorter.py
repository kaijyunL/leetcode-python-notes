# 方法2：按起点排序，重叠时保留结束更早的区间
class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        if len(intervals) <= 1:
            return 0

        intervals.sort(key=lambda item: (item[0], item[1]))
        remove_count = 0
        prev_end = intervals[0][1]

        for start, end in intervals[1:]:
            if start >= prev_end:
                prev_end = end
            else:
                remove_count += 1
                prev_end = min(prev_end, end)

        return remove_count


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
