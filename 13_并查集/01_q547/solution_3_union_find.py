# 方法三：并查集（路径压缩 + 按秩合并，最适合面试）
from typing import List


class UnionFind:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.count = n   # 当前集合数

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])   # 路径压缩
        return self.parent[x]

    def union(self, x: int, y: int) -> bool:
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return False
        # 按秩合并：小树挂到大树下
        if self.rank[rx] < self.rank[ry]:
            rx, ry = ry, rx
        self.parent[ry] = rx
        if self.rank[rx] == self.rank[ry]:
            self.rank[rx] += 1
        self.count -= 1
        return True


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        uf = UnionFind(n)
        for i in range(n):
            for j in range(i + 1, n):   # 只扫上三角
                if isConnected[i][j] == 1:
                    uf.union(i, j)
        return uf.count


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
