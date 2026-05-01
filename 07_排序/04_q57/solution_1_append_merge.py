class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        """
        解法1：追加后排序合并
        时间复杂度: O(n log n)
        空间复杂度: O(n)
        """
        intervals.append(newInterval)
        intervals.sort(key=lambda x: x[0])

        ans = [intervals[0]]

        for s, e in intervals[1:]:
            if s <= ans[-1][1]:
                ans[-1][1] = max(ans[-1][1], e)
            else:
                ans.append([s, e])

        return ans


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        ([[1, 3], [6, 9]], [2, 5]),
        ([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]),
        ([], [5, 7]),
        ([[1, 5]], [2, 3]),
        ([[1, 5]], [2, 7]),
    ]

    for intervals, newInterval in test_cases:
        original = intervals[:]
        print(f"输入: {original}, new={newInterval}, 输出: {solution.insert(intervals, newInterval)}")
