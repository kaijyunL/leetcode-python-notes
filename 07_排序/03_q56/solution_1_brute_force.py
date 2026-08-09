class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        """
        方法1：暴力两两合并
        时间复杂度：最坏 O(n^3)
        空间复杂度：O(n)
        """
        intervals = [iv[:] for iv in intervals]
        ans = []

        while intervals:
            min_index = 0
            for i in range(1, len(intervals)):
                if intervals[i][0] < intervals[min_index][0]:
                    min_index = i

            start, end = intervals.pop(min_index)
            changed = True

            while changed:
                changed = False
                remaining = []

                for next_start, next_end in intervals:
                    if next_start <= end and start <= next_end:
                        start = min(start, next_start)
                        end = max(end, next_end)
                        changed = True
                    else:
                        remaining.append([next_start, next_end])

                intervals = remaining

            ans.append([start, end])

        return ans


if __name__ == "__main__":
    solution = Solution()

    assert solution.merge([[1, 3], [2, 6], [8, 10], [15, 18]]) == [[1, 6], [8, 10], [15, 18]]
    assert solution.merge([[1, 4], [4, 5]]) == [[1, 5]]
    assert solution.merge([[4, 5], [1, 2], [2, 4]]) == [[1, 5]]
    assert solution.merge([[1, 4], [0, 4]]) == [[0, 4]]
    assert solution.merge([]) == []

    print("all tests passed")
