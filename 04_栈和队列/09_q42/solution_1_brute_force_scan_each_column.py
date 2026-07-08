# 方法1：暴力逐列扫描


class Solution:
    def trap(self, height: list[int]) -> int:
        """
        暴力解法：对每个位置向左右各扫一遍找最大值。
        时间复杂度: O(n^2)
        空间复杂度: O(1)
        """
        n = len(height)
        ans = 0

        for i in range(1, n - 1):
            left_max = 0
            right_max = 0

            for j in range(i, -1, -1):
                left_max = max(left_max, height[j])

            for j in range(i, n):
                right_max = max(right_max, height[j])

            ans += min(left_max, right_max) - height[i]

        return ans


def run_test() -> None:
    solver = Solution()
    test_cases = [
        ([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], 6),
        ([4, 2, 0, 3, 2, 5], 9),
        ([1, 2, 3], 0),
        ([3, 2, 1], 0),
        ([], 0),
        ([5], 0),
        ([2, 0, 2], 2),
        ([3, 0, 0, 2, 0, 4], 10),
    ]

    for heights, expected in test_cases:
        result = solver.trap(heights)
        assert result == expected, (
            f"failed for {heights!r}: expected {expected}, got {result}"
        )


if __name__ == "__main__":
    run_test()
    print("all tests passed")
