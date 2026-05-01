class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        """
        解法1：暴力两两合并
        反复扫描，每次合并所有重叠区间对，直到没有可合并的
        时间复杂度: O(n²)
        空间复杂度: O(n)
        """
        intervals = [iv[:] for iv in intervals]

        changed = True
        while changed:
            changed = False
            merged = []
            used = [False] * len(intervals)

            for i in range(len(intervals)):
                if used[i]:
                    continue
                cur = intervals[i][:]

                for j in range(i + 1, len(intervals)):
                    if used[j]:
                        continue
                    if cur[1] >= intervals[j][0] and cur[0] <= intervals[j][1]:
                        cur[0] = min(cur[0], intervals[j][0])
                        cur[1] = max(cur[1], intervals[j][1])
                        used[j] = True
                        changed = True

                merged.append(cur)

            intervals = merged

        return intervals


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        [[1, 3], [2, 6], [8, 10], [15, 18]],
        [[1, 4], [4, 5]],
        [[1, 4], [0, 4]],
        [[1, 4], [2, 3]],
        [[1, 4], [0, 0]],
    ]

    for intervals in test_cases:
        print(f"输入: {intervals}, 输出: {solution.merge(intervals)}")
