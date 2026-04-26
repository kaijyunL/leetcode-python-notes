class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        """
        线性扫描：逐行逐列查找 target
        时间复杂度: O(m * n)
        空间复杂度: O(1)
        """
        for row in matrix:
            for num in row:
                if num == target:
                    return True

        return False


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        ([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3),
        ([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13),
        ([[1]], 1),
        ([[1]], 2),
    ]

    for matrix, target in test_cases:
        print(f"matrix = {matrix}, target = {target}, result = {solution.searchMatrix(matrix, target)}")
