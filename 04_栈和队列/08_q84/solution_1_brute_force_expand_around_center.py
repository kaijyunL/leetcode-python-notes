# 方法1：枚举高度 + 中心扩散


class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        """
        暴力解法：枚举每根柱子作为高度，向左右扩散找第一个更矮的位置。
        时间复杂度: O(n^2)
        空间复杂度: O(1)
        """
        n = len(heights)
        max_area = 0

        for i in range(n):
            height = heights[i]

            # 向左找第一个比 height 矮的位置
            left = i - 1
            while left >= 0 and heights[left] >= height:
                left -= 1

            # 向右找第一个比 height 矮的位置
            right = i + 1
            while right < n and heights[right] >= height:
                right += 1

            # 宽度 = (right - 1) - (left + 1) + 1 = right - left - 1
            width = right - left - 1
            max_area = max(max_area, width * height)

        return max_area


def run_test() -> None:
    solver = Solution()
    test_cases = [
        ([2, 1, 5, 6, 2, 3], 10),
        ([2, 4], 4),
        ([1, 1], 2),
        ([1], 1),
        ([0, 9], 9),
        ([2, 1, 2], 3),
        ([1, 2, 3, 4, 5], 9),
        ([5, 4, 3, 2, 1], 9),
    ]

    for heights, expected in test_cases:
        result = solver.largestRectangleArea(heights)
        assert result == expected, (
            f"failed for {heights!r}: expected {expected}, got {result}"
        )


if __name__ == "__main__":
    run_test()
    print("all tests passed")
