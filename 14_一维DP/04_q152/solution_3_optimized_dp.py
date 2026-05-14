# 方法三：状态压缩
class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        curr_max = nums[0]
        curr_min = nums[0]
        best = nums[0]

        for num in nums[1:]:
            prev_max = curr_max
            prev_min = curr_min
            curr_max = max(num, prev_max * num, prev_min * num)
            curr_min = min(num, prev_max * num, prev_min * num)
            best = max(best, curr_max)

        return best


if __name__ == "__main__":
    solver = Solution()
    test_cases = [
        [2, 3, -2, 4],
        [-2, 0, -1],
        [-2, 3, -4],
        [-2],
    ]

    for nums in test_cases:
        print(f"nums={nums}, max_product={solver.maxProduct(nums)}")
