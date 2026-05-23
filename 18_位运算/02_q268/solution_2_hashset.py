# 方法2：哈希集合


class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        seen = set(nums)
        n = len(nums)

        for num in range(n + 1):
            if num not in seen:
                return num


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
