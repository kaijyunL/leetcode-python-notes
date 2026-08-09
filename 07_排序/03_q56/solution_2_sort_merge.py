class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        """
        方法2：按起点排序 + 一次扫描（面试主推）
        时间复杂度：O(n log n)
        空间复杂度：O(n)
        """
        if not intervals:
            return []

        intervals.sort(key=lambda x: x[0])
        ans = [intervals[0][:]]

        for start, end in intervals[1:]:
            if start <= ans[-1][1]:
                ans[-1][1] = max(ans[-1][1], end)
            else:
                ans.append([start, end])

        return ans


if __name__ == "__main__":
    solution = Solution()

    assert solution.merge([[1, 3], [2, 6], [8, 10], [15, 18]]) == [[1, 6], [8, 10], [15, 18]]
    assert solution.merge([[1, 4], [4, 5]]) == [[1, 5]]
    assert solution.merge([[4, 5], [1, 2], [2, 4]]) == [[1, 5]]
    assert solution.merge([[1, 4], [2, 3]]) == [[1, 4]]
    assert solution.merge([]) == []

    print("all tests passed")
