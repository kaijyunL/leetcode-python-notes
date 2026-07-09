# 方法2：对撞双指针（面试主推）


class Solution:
    def maxArea(self, height: list[int]) -> int:
        """
        对撞双指针：谁矮挪谁，宽只会变小只能指望高变大。
        时间复杂度: O(n)
        空间复杂度: O(1)
        """
        left, right = 0, len(height) - 1
        max_area = 0

        while left < right:
            area = (right - left) * min(height[left], height[right])
            max_area = max(max_area, area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

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
