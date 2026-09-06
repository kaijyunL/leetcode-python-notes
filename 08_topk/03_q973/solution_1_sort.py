class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        """
        方法1：按距离平方排序（基线解法）
        时间复杂度：O(n log n)
        空间复杂度：O(n)
        """
        return sorted(points, key=lambda p: p[0] ** 2 + p[1] ** 2)[:k]


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        ([[1, 3], [-2, 2]], 1, [[-2, 2]]),
        ([[3, 3], [5, -1], [-2, 4]], 2, [[3, 3], [-2, 4]]),
        ([[0, 0], [1, 1]], 1, [[0, 0]]),
        ([[-2, 2], [3, 0], [1, 1]], 2, [[-2, 2], [1, 1]]),
    ]

    for points, k, expected in test_cases:
        assert sorted(solution.kClosest(points, k)) == sorted(expected)

    print("all tests passed")
