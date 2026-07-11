# 方法1：四重循环 + 集合去重

from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums) < 4:
            return []

        nums = sorted(nums)
        n = len(nums)
        seen = set()

        for i in range(n - 3):
            for j in range(i + 1, n - 2):
                for k in range(j + 1, n - 1):
                    for l in range(k + 1, n):
                        if nums[i] + nums[j] + nums[k] + nums[l] == target:
                            seen.add((nums[i], nums[j], nums[k], nums[l]))

        return [list(quadruplet) for quadruplet in sorted(seen)]


def normalize(ans: List[List[int]]) -> List[List[int]]:
    return sorted(ans)


if __name__ == "__main__":
    solution = Solution()

    assert normalize(solution.fourSum([1, 0, -1, 0, -2, 2], 0)) == [
        [-2, -1, 1, 2],
        [-2, 0, 0, 2],
        [-1, 0, 0, 1],
    ]
    assert normalize(solution.fourSum([2, 2, 2, 2, 2], 8)) == [[2, 2, 2, 2]]
    assert normalize(solution.fourSum([0, 0, 0, 0], 0)) == [[0, 0, 0, 0]]
    assert normalize(solution.fourSum([1, 2, 3], 6)) == []
    assert normalize(solution.fourSum([-3, -1, 0, 2, 4, 5], 2)) == [[-3, -1, 2, 4]]

    print("all tests passed")
