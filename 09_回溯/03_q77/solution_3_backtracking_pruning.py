class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        """
        解法3：回溯 + 剪枝 — 面试推荐
        时间复杂度: O(k * C(n,k))
        空间复杂度: O(k * C(n,k))
        """
        ans = []
        path = []

        def backtrack(start: int) -> None:
            if len(path) == k:
                ans.append(path[:])
                return

            remaining = k - len(path)
            for num in range(start, n - remaining + 2):
                path.append(num)
                backtrack(num + 1)
                path.pop()

        backtrack(1)
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
