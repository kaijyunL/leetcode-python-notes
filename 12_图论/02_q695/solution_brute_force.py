from collections import defaultdict
from typing import List, Set, Tuple


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        rows, cols = len(grid), len(grid[0])
        graph = defaultdict(list)
        land_cells = []

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] != 1:
                    continue
                land_cells.append((r, c))
                for dr, dc in ((1, 0), (0, 1)):
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        graph[(r, c)].append((nr, nc))
                        graph[(nr, nc)].append((r, c))

        visited: Set[Tuple[int, int]] = set()

        def dfs(node: Tuple[int, int]) -> int:
            visited.add(node)
            area = 1
            for neighbor in graph[node]:
                if neighbor not in visited:
                    area += dfs(neighbor)
            return area

        max_area = 0
        for cell in land_cells:
            if cell in visited:
                continue
            max_area = max(max_area, dfs(cell))

        return max_area


def run_demo() -> None:
    grid = [
        [0, 0, 1, 0, 0],
        [1, 1, 1, 0, 1],
        [0, 1, 0, 0, 1],
        [0, 0, 0, 1, 1],
    ]
    print(Solution().maxAreaOfIsland(grid))


if __name__ == "__main__":
    run_demo()
