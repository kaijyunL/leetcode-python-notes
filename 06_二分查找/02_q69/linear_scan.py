class Solution:
    def mySqrt(self, x: int) -> int:
        """
        线性扫描：找到第一个平方大于 x 的数
        时间复杂度: O(sqrt(x))
        空间复杂度: O(1)
        """
        i = 0

        while i * i <= x:
            i += 1

        return i - 1


if __name__ == "__main__":
    solution = Solution()

    test_cases = [0, 1, 2, 4, 8, 15, 16]

    for x in test_cases:
        print(f"x = {x}, result = {solution.mySqrt(x)}")
