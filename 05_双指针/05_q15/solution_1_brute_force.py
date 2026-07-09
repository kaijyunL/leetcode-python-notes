# 方法1：三重循环 + 集合去重

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []

        nums = sorted(nums)
        seen = set()
        n = len(nums)

        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if nums[i] + nums[j] + nums[k] == 0:
                        seen.add((nums[i], nums[j], nums[k]))

        return [list(triplet) for triplet in sorted(seen)]


def normalize(result: List[List[int]]) -> List[List[int]]:
    return sorted(result)


if __name__ == "__main__":
    solution = Solution()

    assert normalize(solution.threeSum([-1, 0, 1, 2, -1, -4])) == [[-1, -1, 2], [-1, 0, 1]]
    assert normalize(solution.threeSum([0, 0, 0, 0])) == [[0, 0, 0]]
    assert normalize(solution.threeSum([-2, 0, 0, 2, 2])) == [[-2, 0, 2]]
    assert normalize(solution.threeSum([1, 2, -2, -1])) == []
    assert normalize(solution.threeSum([])) == []

    print("all tests passed")
