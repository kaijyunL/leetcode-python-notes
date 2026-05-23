# 方法4：位运算异或


class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        ans = len(nums)

        for i, num in enumerate(nums):
            ans ^= i
            ans ^= num

        return ans


if __name__ == "__main__":
    solver = Solution()
    test_cases = [
        [3, 0, 1],
        [0, 1],
        [9, 6, 4, 2, 3, 5, 7, 0, 1],
        [0],
    ]

    for nums in test_cases:
        print(f"nums={nums}, answer={solver.missingNumber(nums)}")
