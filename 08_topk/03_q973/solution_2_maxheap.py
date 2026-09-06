import heapq


class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        """
        方法2：大小为 k 的最大堆（Top K 通用解）
        时间复杂度：O(n log k)
        空间复杂度：O(k)
        """
        heap = []

        for x, y in points:
            distance_squared = x * x + y * y

            if len(heap) < k:
                heapq.heappush(heap, (-distance_squared, x, y))
            elif distance_squared < -heap[0][0]:
                heapq.heapreplace(heap, (-distance_squared, x, y))

        return [[x, y] for _, x, y in heap]


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
