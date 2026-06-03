# 方法二：DFS 后序逆序（三色标记 + 反转完成顺序）
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            graph[b].append(a)

        # 0=白(未访问)  1=灰(当前路径上)  2=黑(已完成)
        color = [0] * numCourses
        order = []
        has_cycle = False

        def dfs(u: int) -> None:
            nonlocal has_cycle
            if has_cycle:
                return
            color[u] = 1
            for v in graph[u]:
                if color[v] == 1:    # 灰色 → 有环
                    has_cycle = True
                    return
                if color[v] == 0:
                    dfs(v)
            color[u] = 2
            order.append(u)          # 后序：所有后继处理完才记录自己

        for i in range(numCourses):
            if color[i] == 0:
                dfs(i)
                if has_cycle:
                    return []

        return order[::-1]           # 反转后序就是拓扑序


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
