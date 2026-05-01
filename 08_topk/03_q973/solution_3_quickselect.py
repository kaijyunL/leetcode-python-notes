import random


class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        """
        解法3：快速选择 — 面试推荐
        时间复杂度: O(n) 平均
        空间复杂度: O(1)
        """

        def dist(p):
            return p[0] ** 2 + p[1] ** 2

        left, right = 0, len(points) - 1

        while True:
            pivot = dist(points[random.randint(left, right)])
            lt, i, gt = left, left, right

            while i <= gt:
                if dist(points[i]) < pivot:
                    points[lt], points[i] = points[i], points[lt]
                    lt += 1
                    i += 1
                elif dist(points[i]) > pivot:
                    points[i], points[gt] = points[gt], points[i]
                    gt -= 1
                else:
                    i += 1

            if k <= lt:
                right = lt - 1
            elif k > gt:
                left = gt + 1
            else:
                return points[:k]

        return points[:k]


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        ([[1, 3], [-2, 2]], 1),
        ([[3, 3], [5, -1], [-2, 4]], 2),
        ([[0, 0], [1, 1]], 1),
    ]

    for points, k in test_cases:
        print(f"输入: {points}, k={k}, 输出: {solution.kClosest(points, k)}")
