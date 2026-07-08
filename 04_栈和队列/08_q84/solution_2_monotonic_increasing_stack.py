# 方法2：单调递增栈 + 哨兵


class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        """
        单调递增（非递减）栈 + 哨兵：当前更矮的柱子结算栈顶，栈里存下标。
        时间复杂度: O(n)
        空间复杂度: O(n)
        """
        heights = [0] + heights + [0]
        stack = []
        max_area = 0

        for i, h in enumerate(heights):
            while stack and h < heights[stack[-1]]:
                h_idx = stack.pop()
                height = heights[h_idx]
                width = i - stack[-1] - 1
                max_area = max(max_area, height * width)

            stack.append(i)

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
