class Solution:
    def numTrees(self, n: int) -> int:
        memo = {0: 1, 1: 1}

        def count(nodes: int) -> int:
            if nodes in memo:
                return memo[nodes]

            total = 0
            for root in range(1, nodes + 1):
                # 这里的左右子问题会重复出现，所以适合记忆化
                total += count(root - 1) * count(nodes - root)

            memo[nodes] = total
            return total

        return count(n)


if __name__ == "__main__":
    solution = Solution()
    test_cases = [1, 2, 3, 4, 5]

    for n in test_cases:
        print(f"n = {n}, result = {solution.numTrees(n)}")
