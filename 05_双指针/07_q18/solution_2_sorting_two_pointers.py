# 方法2：排序 + 两层固定 + 双指针（面试主推）

from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums) < 4:
            return []

        nums.sort()
        n = len(nums)
        ans = []

        for i in range(n - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            if nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3] > target:
                break
            if nums[i] + nums[n - 3] + nums[n - 2] + nums[n - 1] < target:
                continue

            for j in range(i + 1, n - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                if nums[i] + nums[j] + nums[j + 1] + nums[j + 2] > target:
                    break
                if nums[i] + nums[j] + nums[n - 2] + nums[n - 1] < target:
                    continue

                left = j + 1
                right = n - 1

                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]

                    if total == target:
                        ans.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                        right -= 1

                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
                    elif total < target:
                        left += 1
                    else:
                        right -= 1

        return ans


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
