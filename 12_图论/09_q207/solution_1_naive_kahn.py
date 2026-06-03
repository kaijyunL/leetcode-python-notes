# 方法一：朴素 Kahn（反复扫描入度为 0 的节点）
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        in_degree = [0] * numCourses
        for a, b in prerequisites:
            graph[b].append(a)
            in_degree[a] += 1

        taken = [False] * numCourses
        count = 0

        while True:
            # 每一轮扫描整张表，找一个还没上、且入度为 0 的课
            found = -1
            for i in range(numCourses):
                if not taken[i] and in_degree[i] == 0:
                    found = i
                    break

            if found == -1:
                break

            taken[found] = True
            count += 1
            for v in graph[found]:
                in_degree[v] -= 1

        return count == numCourses


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
