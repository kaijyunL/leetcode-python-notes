class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        dp_i_2 = 1
        dp_i_1 = 2

        for _ in range(3, n + 1):
            curr = dp_i_2 + dp_i_1
            dp_i_2 = dp_i_1
            dp_i_1 = curr

        return curr


if __name__ == "__main__":
    solver = Solution()
    for n in [1, 2, 3, 4, 5]:
        print(f"n={n}, ways={solver.climbStairs(n)}")
