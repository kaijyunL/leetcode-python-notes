import heapq


class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        """
        解法2：最大堆
        时间复杂度: O(n log k)
        空间复杂度: O(k)
        """
        heap = []

        for x, y in points:
            dist = x * x + y * y
            heapq.heappush(heap, (-dist, x, y))
            if len(heap) > k:
                heapq.heappop(heap)

        return [[x, y] for _, x, y in heap]


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        ([[1, 3], [-2, 2]], 1),
        ([[3, 3], [5, -1], [-2, 4]], 2),
        ([[0, 0], [1, 1]], 1),
    ]

    for points, k in test_cases:
        print(f"输入: {points}, k={k}, 输出: {solution.kClosest(points, k)}")
