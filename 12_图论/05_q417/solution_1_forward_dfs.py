# 方法1：从每个格子正向 DFS（直观但会重复搜索）
# 时间复杂度：O((mn)^2)，空间复杂度：O(mn)

from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []

        rows, cols = len(heights), len(heights[0])
        answer = []

        def can_reach(r, c, ocean):
            visited = [[False] * cols for _ in range(rows)]

            def dfs(r, c):
                if ocean == "pacific" and (r == 0 or c == 0):
                    return True
                if ocean == "atlantic" and (r == rows - 1 or c == cols - 1):
                    return True

                visited[r][c] = True

                for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nr, nc = r + dr, c + dc
                    if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
                        continue
                    if visited[nr][nc] or heights[nr][nc] > heights[r][c]:
                        continue
                    if dfs(nr, nc):
                        return True

                return False

            return dfs(r, c)

        for r in range(rows):
            for c in range(cols):
                if can_reach(r, c, "pacific") and can_reach(r, c, "atlantic"):
                    answer.append([r, c])

        return answer


def run_demo() -> None:
    heights = [
        [1, 2, 2, 3, 5],
        [3, 2, 3, 4, 4],
        [2, 4, 5, 3, 1],
        [6, 7, 1, 4, 5],
        [5, 1, 1, 2, 4],
    ]
    print(Solution().pacificAtlantic(heights))


if __name__ == "__main__":
    run_demo()
