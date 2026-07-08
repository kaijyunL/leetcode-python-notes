# 方法3：双指针（面试主推）


class Solution:
    def trap(self, height: list[int]) -> int:
        """
        双指针：哪边矮就结算哪边，另一边一定有更高的挡板兜底。
        时间复杂度: O(n)
        空间复杂度: O(1)
        """
        if not height:
            return 0

        left, right = 0, len(height) - 1
        left_max, right_max = 0, 0
        ans = 0

        while left < right:
            left_max = max(left_max, height[left])
            right_max = max(right_max, height[right])

            if left_max < right_max:
                ans += left_max - height[left]
                left += 1
            else:
                ans += right_max - height[right]
                right -= 1

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
