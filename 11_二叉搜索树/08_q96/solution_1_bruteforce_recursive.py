class Solution:
    def numTrees(self, n: int) -> int:
        def count(nodes: int) -> int:
            if nodes <= 1:
                return 1

            total = 0
            for root in range(1, nodes + 1):
                # 固定当前根节点后，左右子树方案数相乘
                left_count = count(root - 1)
                right_count = count(nodes - root)
                total += left_count * right_count
            return total

        return count(n)


if __name__ == "__main__":
    solution = Solution()
    test_cases = [1, 2, 3, 4]

    for n in test_cases:
        print(f"n = {n}, result = {solution.numTrees(n)}")
