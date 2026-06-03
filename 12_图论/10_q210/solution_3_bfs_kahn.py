# 方法三：BFS + Kahn 算法（队列优化，最适合面试）
from collections import deque
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        in_degree = [0] * numCourses
        for a, b in prerequisites:
            graph[b].append(a)
            in_degree[a] += 1

        queue = deque(i for i in range(numCourses) if in_degree[i] == 0)
        order = []

        while queue:
            u = queue.popleft()
            order.append(u)
            for v in graph[u]:
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    queue.append(v)

        return order if len(order) == numCourses else []


def run_demo() -> None:
    cases = [
        (2, [[1, 0]]),
        (4, [[1, 0], [2, 0], [3, 1], [3, 2]]),
        (1, []),
        (2, [[1, 0], [0, 1]]),
        (3, [[0, 1], [1, 2], [2, 0]]),
    ]
    for n, pre in cases:
        got = Solution().findOrder(n, pre)
        print(f"numCourses={n}, prerequisites={pre} -> {got}")


if __name__ == "__main__":
    run_demo()
