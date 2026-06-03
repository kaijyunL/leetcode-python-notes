# 方法一：朴素 Kahn（反复扫描入度为 0 的节点）
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        in_degree = [0] * numCourses
        for a, b in prerequisites:
            graph[b].append(a)
            in_degree[a] += 1

        taken = [False] * numCourses
        order = []

        while True:
            found = -1
            for i in range(numCourses):
                if not taken[i] and in_degree[i] == 0:
                    found = i
                    break

            if found == -1:
                break

            taken[found] = True
            order.append(found)
            for v in graph[found]:
                in_degree[v] -= 1

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
