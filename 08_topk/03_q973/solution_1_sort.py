class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        """
        解法1：排序后取前 k
        时间复杂度: O(n log n)
        空间复杂度: O(1)
        """
        return sorted(points, key=lambda p: p[0] ** 2 + p[1] ** 2)[:k]


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        ([[1, 3], [-2, 2]], 1),
        ([[3, 3], [5, -1], [-2, 4]], 2),
        ([[0, 0], [1, 1]], 1),
    ]

    for points, k in test_cases:
        print(f"输入: {points}, k={k}, 输出: {solution.kClosest(points, k)}")
