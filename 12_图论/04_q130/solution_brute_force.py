from typing import List, Set, Tuple


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board or not board[0]:
            return

        rows, cols = len(board), len(board[0])
        visited_global: Set[Tuple[int, int]] = set()

        for r in range(rows):
            for c in range(cols):
                if board[r][c] != "O" or (r, c) in visited_global:
                    continue

                region = []
                seen = set()
                touches_border = False
                stack = [(r, c)]

                while stack:
                    x, y = stack.pop()
                    if (x, y) in seen or board[x][y] != "O":
                        continue

                    seen.add((x, y))
                    region.append((x, y))

                    if x == 0 or x == rows - 1 or y == 0 or y == cols - 1:
                        touches_border = True

                    for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < rows and 0 <= ny < cols and (nx, ny) not in seen:
                            stack.append((nx, ny))

                visited_global |= seen

                if touches_border:
                    continue

                for x, y in region:
                    board[x][y] = "X"


def run_demo() -> None:
    board = [
        ["X", "X", "X", "X"],
        ["X", "O", "O", "X"],
        ["X", "X", "O", "X"],
        ["X", "O", "X", "X"],
    ]
    Solution().solve(board)
    for row in board:
        print(row)


if __name__ == "__main__":
    run_demo()
