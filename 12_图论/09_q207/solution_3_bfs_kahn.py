# 方法三：BFS + Kahn 算法（队列优化，最适合面试）
from collections import deque
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        in_degree = [0] * numCourses
        for a, b in prerequisites:
            graph[b].append(a)
            in_degree[a] += 1

        # 所有入度为 0 的课同时入队
        queue = deque(i for i in range(numCourses) if in_degree[i] == 0)
        taken = 0

        while queue:
            u = queue.popleft()
            taken += 1
            for v in graph[u]:
                in_degree[v] -= 1
                if in_degree[v] == 0:   # 入度刚降到 0 才入队
                    queue.append(v)

        return taken == numCourses


def run_demo() -> None:
    cases = [
        (2, [[1, 0]], True),
        (2, [[1, 0], [0, 1]], False),
        (4, [[1, 0], [2, 0], [3, 1], [3, 2]], True),
        (3, [[0, 1], [1, 2], [2, 0]], False),
    ]
    for n, pre, expected in cases:
        got = Solution().canFinish(n, pre)
        print(f"numCourses={n}, prerequisites={pre} -> {got} (期望 {expected})")


if __name__ == "__main__":
    run_demo()
