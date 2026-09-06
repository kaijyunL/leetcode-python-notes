import random


class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        """
        方法3：三路快速选择（复杂度优化主解）
        时间复杂度：平均 O(n)，最坏 O(n^2)
        空间复杂度：O(1) 额外空间
        """
        def distance_squared(point):
            return point[0] * point[0] + point[1] * point[1]

        target = k - 1
        left, right = 0, len(points) - 1

        while True:
            pivot = points[random.randint(left, right)]
            pivot_distance = distance_squared(pivot)
            less_end = left
            i = left
            greater_start = right

            # 分区后：[left, less_end - 1] < pivot，
            # [less_end, greater_start] == pivot，
            # [greater_start + 1, right] > pivot。
            while i <= greater_start:
                current_distance = distance_squared(points[i])

                if current_distance < pivot_distance:
                    points[less_end], points[i] = points[i], points[less_end]
                    less_end += 1
                    i += 1
                elif current_distance > pivot_distance:
                    points[i], points[greater_start] = points[greater_start], points[i]
                    greater_start -= 1
                else:
                    i += 1

            if target < less_end:
                right = less_end - 1
            elif target > greater_start:
                left = greater_start + 1
            else:
                return points[:k]


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        ([[1, 3], [-2, 2]], 1, [[-2, 2]]),
        ([[3, 3], [5, -1], [-2, 4]], 2, [[3, 3], [-2, 4]]),
        ([[0, 0], [1, 1]], 1, [[0, 0]]),
        ([[-2, 2], [3, 0], [1, 1]], 2, [[-2, 2], [1, 1]]),
    ]

    for points, k, expected in test_cases:
        actual = solution.kClosest([point[:] for point in points], k)
        assert sorted(actual) == sorted(expected)

    print("all tests passed")
