class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        """
        最优解法：把二维矩阵当作一维升序数组后二分
        时间复杂度: O(log(m * n))
        空间复杂度: O(1)
        """
        rows = len(matrix)
        cols = len(matrix[0])
        left = 0
        right = rows * cols - 1

        while left <= right:
            mid = (left + right) // 2
            num = matrix[mid // cols][mid % cols]

            if num < target:
                left = mid + 1
            else:
                right = mid - 1

        index = right + 1
        if index == rows * cols:
            return False

        return matrix[index // cols][index % cols] == target


class SolutionStandardTemplate:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        """
        标准模板写法：把二维矩阵当作一维数组，找到 target 直接返回
        时间复杂度: O(log(m * n))
        空间复杂度: O(1)
        """
        rows = len(matrix)
        cols = len(matrix[0])
        left = 0
        right = rows * cols - 1

        while left <= right:
            mid = (left + right) // 2
            num = matrix[mid // cols][mid % cols]

            if num == target:
                return True
            elif num < target:
                left = mid + 1
            else:
                right = mid - 1

        return False


class SolutionLessOrEqual:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        """
        变体写法：找最后一个小于等于 target 的位置
        """
        rows = len(matrix)
        cols = len(matrix[0])
        left = 0
        right = rows * cols - 1

        while left <= right:
            mid = (left + right) // 2
            num = matrix[mid // cols][mid % cols]

            if num <= target:
                left = mid + 1
            else:
                right = mid - 1

        if right < 0:
            return False

        return matrix[right // cols][right % cols] == target


if __name__ == "__main__":
    solution = Solution()
    solution_standard_template = SolutionStandardTemplate()
    solution_less_or_equal = SolutionLessOrEqual()

    test_cases = [
        ([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3),
        ([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13),
        ([[1]], 1),
        ([[1]], 2),
    ]

    for matrix, target in test_cases:
        print(f"matrix = {matrix}, target = {target}, result = {solution.searchMatrix(matrix, target)}")
        print(f"标准模板 result = {solution_standard_template.searchMatrix(matrix, target)}")
        print(f"<= 写法 result = {solution_less_or_equal.searchMatrix(matrix, target)}")
