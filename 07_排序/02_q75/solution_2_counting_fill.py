class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        解法2：两次计数填充
        时间复杂度: O(n)，需要两趟扫描
        空间复杂度: O(1)
        """
        cnt0 = cnt1 = cnt2 = 0

        for x in nums:
            if x == 0:
                cnt0 += 1
            elif x == 1:
                cnt1 += 1
            else:
                cnt2 += 1

        for i in range(cnt0):
            nums[i] = 0
        for i in range(cnt0, cnt0 + cnt1):
            nums[i] = 1
        for i in range(cnt0 + cnt1, len(nums)):
            nums[i] = 2


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
