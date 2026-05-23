# 方法3：Brian Kernighan 算法


class Solution:
    def hammingWeight(self, n: int) -> int:
        ans = 0

        while n:
            n &= n - 1
            ans += 1

        return ans


if __name__ == "__main__":
    solver = Solution()
    test_cases = [11, 128, 0, 7]

    for n in test_cases:
        print(f"n={n}, answer={solver.hammingWeight(n)}")
