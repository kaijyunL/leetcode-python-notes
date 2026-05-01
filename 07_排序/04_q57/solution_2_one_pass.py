class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        """
        解法2：一趟扫描（三段法）— 面试推荐
        时间复杂度: O(n)
        空间复杂度: O(n)
        """
        ans = []
        newStart, newEnd = newInterval
        inserted = False

        for s, e in intervals:
            if e < newStart:
                ans.append([s, e])
            elif s > newEnd:
                if not inserted:
                    ans.append([newStart, newEnd])
                    inserted = True
                ans.append([s, e])
            else:
                newStart = min(newStart, s)
                newEnd = max(newEnd, e)

        if not inserted:
            ans.append([newStart, newEnd])

        return ans


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        ([[1, 3], [6, 9]], [2, 5]),
        ([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]),
        ([], [5, 7]),
        ([[1, 5]], [2, 3]),
        ([[1, 5]], [2, 7]),
        ([[2, 3], [5, 7]], [0, 1]),
        ([[2, 3], [5, 7]], [8, 9]),
    ]

    for intervals, newInterval in test_cases:
        print(f"输入: {intervals}, new={newInterval}, 输出: {solution.insert(intervals, newInterval)}")
