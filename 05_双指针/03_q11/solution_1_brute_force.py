# 方法1：暴力枚举


class Solution:
    def maxArea(self, height: list[int]) -> int:
        """
        暴力：枚举所有两两组合算面积。
        时间复杂度: O(n^2)
        空间复杂度: O(1)
        """
        n = len(height)
        max_area = 0

        for i in range(n):
            for j in range(i + 1, n):
                area = (j - i) * min(height[i], height[j])
                max_area = max(max_area, area)

        return max_area


def run_test() -> None:
    solver = Solution()

    assert solver.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
    assert solver.maxArea([1, 1]) == 1
    assert solver.maxArea([4, 3, 2, 1, 4]) == 16
    assert solver.maxArea([1, 2, 1]) == 2
    assert solver.maxArea([2, 3, 4, 5, 18, 17, 6]) == 17


if __name__ == "__main__":
    run_test()
    print("all tests passed")
