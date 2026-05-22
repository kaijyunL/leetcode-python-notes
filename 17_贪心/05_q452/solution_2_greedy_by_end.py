# 方法2：按右端点排序的贪心
class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        if not points:
            return 0

        points.sort(key=lambda item: item[1])
        arrows = 1
        arrow_pos = points[0][1]

        for start, end in points[1:]:
            if start > arrow_pos:
                arrows += 1
                arrow_pos = end

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
