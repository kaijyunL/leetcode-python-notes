# 方法2：DP 预处理左右最大值


class Solution:
    def trap(self, height: list[int]) -> int:
        """
        DP 预处理：用两个数组分别记录每个位置的左侧最大值和右侧最大值。
        时间复杂度: O(n)
        空间复杂度: O(n)
        """
        if not height:
            return 0

        n = len(height)
        left_max = [0] * n
        right_max = [0] * n

        left_max[0] = height[0]
        for i in range(1, n):
            left_max[i] = max(left_max[i - 1], height[i])

        right_max[n - 1] = height[n - 1]
        for i in range(n - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], height[i])

        ans = 0
        for i in range(n):
            ans += min(left_max[i], right_max[i]) - height[i]

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
