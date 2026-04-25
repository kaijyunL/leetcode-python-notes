from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        """
        暴力解法：枚举所有三元组
        时间复杂度: O(n^3)
        空间复杂度: O(1)
        """
        n = len(nums)
        res = nums[0] + nums[1] + nums[2]

        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    total = nums[i] + nums[j] + nums[k]

                    if abs(total - target) < abs(res - target):
                        res = total

        return res


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        ([-1, 2, 1, -4], 1),
        ([0, 0, 0], 1),
        ([1, 1, 1, 0], -100),
    ]

    for nums, target in test_cases:
        print(f"nums = {nums}, target = {target}, result = {solution.threeSumClosest(nums, target)}")
