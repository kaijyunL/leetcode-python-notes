# 方法3：位运算异或


class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        ans = 0

        for num in nums:
            ans ^= num

        return ans


if __name__ == "__main__":
    solver = Solution()
    test_cases = [
        [2, 2, 1],
        [4, 1, 2, 1, 2],
        [1],
        [-1, -1, -2],
    ]

    for nums in test_cases:
        print(f"nums={nums}, answer={solver.singleNumber(nums)}")
