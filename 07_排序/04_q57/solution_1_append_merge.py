class Solution:
    def insert(self, intervals: list[list[int]], new_interval: list[int]) -> list[list[int]]:
        """
        方法1：追加后排序合并
        时间复杂度：O(n log n)
        空间复杂度：O(n)
        """
        all_intervals = [interval[:] for interval in intervals]
        all_intervals.append(new_interval[:])
        all_intervals.sort(key=lambda interval: interval[0])

        ans = [all_intervals[0]]

        for start, end in all_intervals[1:]:
            if start <= ans[-1][1]:
                ans[-1][1] = max(ans[-1][1], end)
            else:
                ans.append([start, end])

        return ans


if __name__ == "__main__":
    solution = Solution()

    assert solution.insert([[1, 3], [6, 9]], [2, 5]) == [[1, 5], [6, 9]]
    assert solution.insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]) == [[1, 2], [3, 10], [12, 16]]
    assert solution.insert([], [5, 7]) == [[5, 7]]
    assert solution.insert([[2, 3], [5, 7]], [0, 1]) == [[0, 1], [2, 3], [5, 7]]
    assert solution.insert([[2, 3], [5, 7]], [8, 9]) == [[2, 3], [5, 7], [8, 9]]

    print("all tests passed")
