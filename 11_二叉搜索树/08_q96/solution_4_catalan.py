class Solution:
    def numTrees(self, n: int) -> int:
        catalan = 1

        for i in range(n):
            # 迭代计算卡特兰数，避免浮点误差
            catalan = catalan * 2 * (2 * i + 1) // (i + 2)

        return catalan


if __name__ == "__main__":
    solution = Solution()
    test_cases = [1, 2, 3, 4, 5]

    for n in test_cases:
        print(f"n = {n}, result = {solution.numTrees(n)}")
