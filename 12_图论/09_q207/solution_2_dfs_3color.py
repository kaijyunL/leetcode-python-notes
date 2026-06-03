# 方法二：DFS + 三色标记（白/灰/黑）
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            graph[b].append(a)

        # 0=白(未访问)  1=灰(当前路径上)  2=黑(已确认无环)
        color = [0] * numCourses

        def dfs(u: int) -> bool:
            if color[u] == 1:   # 灰：路径上又见到自己 → 有环
                return False
            if color[u] == 2:   # 黑：已经验证过，直接跳过
                return True

            color[u] = 1
            for v in graph[u]:
                if not dfs(v):
                    return False
            color[u] = 2
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True


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
