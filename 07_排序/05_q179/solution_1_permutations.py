from itertools import permutations


class Solution:
    def largestNumber(self, nums: list[int]) -> str:
        """
        解法1：全排列枚举
        时间复杂度: O(n!)
        空间复杂度: O(n)
        """
        ans = "0"

        for perm in permutations(nums):
            candidate = "".join(str(x) for x in perm)
            if candidate > ans:
                ans = candidate

        return ans


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        [10, 2],
        [3, 30, 34, 5, 9],
        [0, 0],
        [1],
        [10, 10],
    ]

    for nums in test_cases:
        print(f"输入: {nums}, 输出: {solution.largestNumber(nums)}")
