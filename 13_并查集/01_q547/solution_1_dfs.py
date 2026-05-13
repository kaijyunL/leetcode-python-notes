# 方法一：DFS（从每个未访问城市出发遍历整个连通块）
from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = [False] * n
        provinces = 0

        def dfs(i: int) -> None:
            for j in range(n):
                if isConnected[i][j] == 1 and not visited[j]:
                    visited[j] = True
                    dfs(j)

        for i in range(n):
            if not visited[i]:
                provinces += 1
                visited[i] = True
                dfs(i)

        return provinces


def run_demo() -> None:
    cases = [
        ([[1, 1, 0], [1, 1, 0], [0, 0, 1]], 2),
        ([[1, 0, 0], [0, 1, 0], [0, 0, 1]], 3),
        ([[1, 1, 0, 0], [1, 1, 1, 0], [0, 1, 1, 0], [0, 0, 0, 1]], 2),
        ([[1]], 1),
    ]
    for mat, expected in cases:
        got = Solution().findCircleNum(mat)
        print(f"isConnected={mat} -> {got} (期望 {expected})")


if __name__ == "__main__":
    run_demo()
