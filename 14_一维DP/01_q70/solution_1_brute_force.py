class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)


if __name__ == "__main__":
    solver = Solution()
    for n in [1, 2, 3, 4, 5]:
        print(f"n={n}, ways={solver.climbStairs(n)}")
