# 方法四：BFS
from collections import deque


class Solution:
    def numSquares(self, n: int) -> int:
        squares = []
        i = 1
        while i * i <= n:
            squares.append(i * i)
            i += 1

        queue = deque([0])
        visited = {0}
        steps = 0

        while queue:
            steps += 1

            for _ in range(len(queue)):
                total = queue.popleft()

                for square in squares:
                    nxt = total + square
                    if nxt == n:
                        return steps
                    if nxt > n:
                        break
                    if nxt not in visited:
                        visited.add(nxt)
                        queue.append(nxt)

        return 0


if __name__ == "__main__":
    solver = Solution()
    for n in (1, 12, 13, 43):
        print(f"n={n}, count={solver.numSquares(n)}")
