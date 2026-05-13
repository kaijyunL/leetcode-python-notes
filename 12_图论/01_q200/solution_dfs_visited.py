from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        rows, cols = len(grid), len(grid[0])
        visited = [[False] * cols for _ in range(rows)]

        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return
            if grid[r][c] != "1" or visited[r][c]:
                return

            visited[r][c] = True

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        islands = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] != "1" or visited[r][c]:
                    continue
                islands += 1
                dfs(r, c)

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
