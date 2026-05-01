class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        """
        解法2：排序 + 一次扫描 — 面试推荐
        时间复杂度: O(n log n)
        空间复杂度: O(n)
        """
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
        [[1, 3], [2, 6], [8, 10], [15, 18]],
        [[1, 4], [4, 5]],
        [[1, 4], [0, 4]],
        [[1, 4], [2, 3]],
        [[1, 4], [0, 0]],
        [],
    ]

    for intervals in test_cases:
        print(f"输入: {intervals}, 输出: {solution.merge(intervals)}")
