from collections import defaultdict
from typing import List, Set, Tuple


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        rows, cols = len(grid), len(grid[0])
        graph = defaultdict(list)
        land_cells = []

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] != "1":
                    continue
                land_cells.append((r, c))
                for dr, dc in ((1, 0), (0, 1)):
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "1":
                        graph[(r, c)].append((nr, nc))
                        graph[(nr, nc)].append((r, c))

        visited: Set[Tuple[int, int]] = set()
        islands = 0

        def dfs(node: Tuple[int, int]) -> None:
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs(neighbor)

        for cell in land_cells:
            if cell in visited:
                continue
            islands += 1
            dfs(cell)

        return islands


def run_demo() -> None:
    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"],
    ]
    print(Solution().numIslands(grid))


if __name__ == "__main__":
    run_demo()
