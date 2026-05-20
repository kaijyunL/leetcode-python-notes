# 方法一：暴力枚举 + 滚动乘积
class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        n = len(nums)
        best = nums[0]

        for i in range(n):
            prod = 1
            for j in range(i, n):
                prod *= nums[j]
                best = max(best, prod)

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
