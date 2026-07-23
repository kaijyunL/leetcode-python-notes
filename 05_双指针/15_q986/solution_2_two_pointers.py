# 方法2：双指针推进（面试主推）

from typing import List


class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        i = 0
        j = 0
        ans = []

        while i < len(firstList) and j < len(secondList):
            a_start, a_end = firstList[i]
            b_start, b_end = secondList[j]

            start = max(a_start, b_start)
            end = min(a_end, b_end)

            if start <= end:
                ans.append([start, end])

            if a_end < b_end:
                i += 1
            else:
                j += 1

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
