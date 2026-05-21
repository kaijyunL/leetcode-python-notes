# 方法2：按区间推进
class Solution:
    def jump(self, nums: list[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0

        steps = 0
        start = 0
        end = 0

        while end < n - 1:
            max_pos = end

            for i in range(start, end + 1):
                max_pos = max(max_pos, i + nums[i])

            steps += 1
            start = end + 1
            end = max_pos

        return steps


if __name__ == "__main__":
    solver = Solution()
    test_cases = [
        [2, 3, 1, 1, 4],
        [2, 3, 0, 1, 4],
        [1],
        [1, 2],
        [1, 1, 1, 1],
        [4, 1, 1, 3, 1, 1, 1],
    ]

    for nums in test_cases:
        print(f"nums={nums}, min_jumps={solver.jump(nums)}")
