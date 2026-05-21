# 方法二：贪心维护最远可达位置
class Solution:
    def canJump(self, nums: list[int]) -> bool:
        farthest = 0

        for i, step in enumerate(nums):
            if i > farthest:
                return False

            farthest = max(farthest, i + step)
            if farthest >= len(nums) - 1:
                return True

        return True


if __name__ == "__main__":
    solver = Solution()
    test_cases = [
        [2, 3, 1, 1, 4],
        [3, 2, 1, 0, 4],
        [0],
        [2, 0, 0],
        [1, 0, 1, 0],
    ]

    for nums in test_cases:
        print(f"nums={nums}, can_jump={solver.canJump(nums)}")
