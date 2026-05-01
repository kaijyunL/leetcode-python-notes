class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        解法3：一趟三指针（荷兰国旗问题）— 面试推荐
        时间复杂度: O(n)
        空间复杂度: O(1)
        """
        p0 = 0   # 下一个 0 的放置位置
        i = 0    # 当前检查位置
        p2 = len(nums) - 1  # 下一个 2 的放置位置

        while i <= p2:
            if nums[i] == 0:
                nums[p0], nums[i] = nums[i], nums[p0]
                p0 += 1
                i += 1
            elif nums[i] == 2:
                nums[i], nums[p2] = nums[p2], nums[i]
                p2 -= 1
                # i 不前进，需要重新检查从 p2 换过来的元素
            else:
                i += 1


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        [2, 0, 2, 1, 1, 0],
        [2, 0, 1],
        [0],
        [1],
        [2],
        [0, 0, 0],
        [1, 2, 0, 1, 2, 0],
    ]

    for nums in test_cases:
        original = nums[:]
        solution.sortColors(nums)
        print(f"输入: {original}, 输出: {nums}")
