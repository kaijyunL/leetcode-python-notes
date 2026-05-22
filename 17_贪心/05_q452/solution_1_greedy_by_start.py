# 方法1：按起点排序，维护当前公共射击区间
class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        if not points:
            return 0

        points.sort(key=lambda item: (item[0], item[1]))
        arrows = 1
        overlap_end = points[0][1]

        for start, end in points[1:]:
            if start > overlap_end:
                arrows += 1
                overlap_end = end
            else:
                overlap_end = min(overlap_end, end)

        return arrows


if __name__ == "__main__":
    solver = Solution()
    test_cases = [
        [[10, 16], [2, 8], [1, 6], [7, 12]],
        [[1, 2], [3, 4], [5, 6], [7, 8]],
        [[1, 2], [2, 3], [3, 4], [4, 5]],
        [[1, 10], [2, 9], [3, 8], [4, 7]],
        [[-2147483648, 2147483647], [1, 2], [2, 3]],
    ]

    for points in test_cases:
        print(f"points={points}, arrows={solver.findMinArrowShots(points)}")
