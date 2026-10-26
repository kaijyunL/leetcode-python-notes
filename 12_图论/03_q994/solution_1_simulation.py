# 方法1：逐分钟模拟（直观但较慢）
# 时间复杂度：O((mn)^2)，空间复杂度：O(mn)

from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        fresh = sum(cell == 1 for row in grid for cell in row)
        minutes = 0

        while fresh:
            to_rot = []

            for r in range(rows):
                for c in range(cols):
                    if grid[r][c] != 2:
                        continue

                    for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        nr, nc = r + dr, c + dc
                        if (
                            0 <= nr < rows
                            and 0 <= nc < cols
                            and grid[nr][nc] == 1
                        ):
                            to_rot.append((nr, nc))

            if not to_rot:
                return -1

            for r, c in to_rot:
                if grid[r][c] == 1:
                    grid[r][c] = 2
                    fresh -= 1

            minutes += 1

        return minutes
