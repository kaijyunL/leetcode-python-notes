from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        rows, cols = len(grid), len(grid[0])

        def dfs(r: int, c: int) -> int:
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return 0
            if grid[r][c] != 1:
                return 0

            grid[r][c] = 0

            return (
                1
                + dfs(r + 1, c)
                + dfs(r - 1, c)
                + dfs(r, c + 1)
                + dfs(r, c - 1)
            )

        max_area = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] != 1:
                    continue
                max_area = max(max_area, dfs(r, c))

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
