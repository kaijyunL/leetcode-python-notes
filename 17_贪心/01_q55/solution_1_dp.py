# 方法一：动态规划
class Solution:
    def canJump(self, nums: list[int]) -> bool:
        n = len(nums)
        good = [False] * n
        good[-1] = True

        for i in range(n - 2, -1, -1):
            farthest = min(n - 1, i + nums[i])
            for j in range(i + 1, farthest + 1):
                if good[j]:
                    good[i] = True
                    break

        return good[0]


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
