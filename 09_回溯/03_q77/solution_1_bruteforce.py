class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        """
        解法1：暴力枚举所有子集，保留长度为 k 的组合
        时间复杂度: O(n * 2^n)
        空间复杂度: O(k * C(n,k))
        """
        ans = []

        for mask in range(1 << n):
            path = []
            for i in range(n):
                if mask & (1 << i):
                    path.append(i + 1)

            if len(path) == k:
                ans.append(path)

        return ans


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        (4, 2),
        (1, 1),
        (5, 3),
    ]

    for n, k in test_cases:
        print(f"输入: n={n}, k={k}, 输出: {solution.combine(n, k)}")
