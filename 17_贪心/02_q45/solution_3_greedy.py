# 方法3：压缩贪心
class Solution:
    def jump(self, nums: list[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0

        steps = 0
        current_end = 0  # 当前这一步覆盖的右边界
        farthest = 0  # 当前区间里，下一步能抵达的右边界

        for i in range(n - 1):
            farthest = max(farthest, i + nums[i])

            if i == current_end:
                steps += 1
                current_end = farthest

        return steps


if __name__ == "__main__":
    solver = Solution()
    test_cases = [
        [2, 3, 1, 1, 4],
        [2, 3, 0, 1, 4],
        [1],
        [1, 2],
        [1, 1, 1, 1],
    ]

    for nums in test_cases:
        print(f"nums={nums}, min_jumps={solver.jump(nums)}")
