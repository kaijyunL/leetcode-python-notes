# 方法1：两层枚举所有区间对

from typing import List


class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        ans = []

        for a_start, a_end in firstList:
            for b_start, b_end in secondList:
                start = max(a_start, b_start)
                end = min(a_end, b_end)

                if start <= end:
                    ans.append([start, end])

        return ans


if __name__ == "__main__":
    solution = Solution()

    assert solution.intervalIntersection(
        [[0, 2], [5, 10], [13, 23], [24, 25]],
        [[1, 5], [8, 12], [15, 24], [25, 26]],
    ) == [[1, 2], [5, 5], [8, 10], [15, 23], [24, 24], [25, 25]]
    assert solution.intervalIntersection([[1, 3], [5, 9]], []) == []
    assert solution.intervalIntersection([], [[4, 8], [10, 12]]) == []
    assert solution.intervalIntersection([[1, 7]], [[3, 10]]) == [[3, 7]]
    assert solution.intervalIntersection([[1, 2], [6, 8]], [[3, 5]]) == []

    print("all tests passed")
