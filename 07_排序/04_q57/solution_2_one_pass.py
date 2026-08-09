class Solution:
    def insert(self, intervals: list[list[int]], new_interval: list[int]) -> list[list[int]]:
        """
        方法2：一趟三段扫描（面试主推）
        时间复杂度：O(n)
        空间复杂度：O(n)
        """
        ans = []
        start, end = new_interval
        i = 0

        while i < len(intervals) and intervals[i][1] < start:
            ans.append(intervals[i])
            i += 1

        while i < len(intervals) and intervals[i][0] <= end:
            start = min(start, intervals[i][0])
            end = max(end, intervals[i][1])
            i += 1

        ans.append([start, end])
        ans.extend(intervals[i:])

        return ans


if __name__ == "__main__":
    solution = Solution()

    assert solution.insert([[1, 3], [6, 9]], [2, 5]) == [[1, 5], [6, 9]]
    assert solution.insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]) == [[1, 2], [3, 10], [12, 16]]
    assert solution.insert([], [5, 7]) == [[5, 7]]
    assert solution.insert([[1, 5]], [2, 3]) == [[1, 5]]
    assert solution.insert([[2, 3], [5, 7]], [0, 1]) == [[0, 1], [2, 3], [5, 7]]
    assert solution.insert([[2, 3], [5, 7]], [8, 9]) == [[2, 3], [5, 7], [8, 9]]

    print("all tests passed")
