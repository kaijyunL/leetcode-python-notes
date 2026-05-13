# 方法二：BFS（队列迭代版，避免递归栈）
from collections import deque
from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = [False] * n
        provinces = 0

        for i in range(n):
            if visited[i]:
                continue
            provinces += 1
            queue = deque([i])
            visited[i] = True
            while queue:
                cur = queue.popleft()
                for j in range(n):
                    if isConnected[cur][j] == 1 and not visited[j]:
                        visited[j] = True
                        queue.append(j)

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
