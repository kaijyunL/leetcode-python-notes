class Solution:
    def mySqrt(self, x: int) -> int:
        """
        最优解法：二分查找最后一个平方小于等于 x 的位置
        时间复杂度: O(log x)
        空间复杂度: O(1)
        """
        left = 0
        right = x

        while left <= right:
            mid = (left + right) // 2
            square = mid * mid

            if square <= x:
                left = mid + 1
            else:
                right = mid - 1

        return right


class SolutionStandardTemplate:
    def mySqrt(self, x: int) -> int:
        """
        标准模板写法：先判断 mid * mid 是否等于 x
        时间复杂度: O(log x)
        空间复杂度: O(1)
        """
        left = 0
        right = x

        while left <= right:
            mid = (left + right) // 2
            square = mid * mid

            if square == x:
                return mid
            elif square < x:
                left = mid + 1
            else:
                right = mid - 1

        return right


if __name__ == "__main__":
    solution = Solution()
    solution_standard_template = SolutionStandardTemplate()

    test_cases = [0, 1, 2, 4, 8, 15, 16, 2147395599]

    for x in test_cases:
        print(f"x = {x}, result = {solution.mySqrt(x)}")
        print(f"标准模板 result = {solution_standard_template.mySqrt(x)}")
