# 方法2：排序 + 双指针（面试主推）

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []

        nums.sort()
        ans = []
        n = len(nums)

        for i in range(n - 2):
            if nums[i] > 0:
                break

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = n - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    ans.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1

        return ans


def normalize(ans: List[List[int]]) -> List[List[int]]:
    return sorted(ans)


if __name__ == "__main__":
    solution = Solution()

    assert normalize(solution.threeSum([-1, 0, 1, 2, -1, -4])) == [[-1, -1, 2], [-1, 0, 1]]
    assert normalize(solution.threeSum([0, 0, 0, 0])) == [[0, 0, 0]]
    assert normalize(solution.threeSum([-2, 0, 0, 2, 2])) == [[-2, 0, 2]]
    assert normalize(solution.threeSum([1, 2, -2, -1])) == []
    assert normalize(solution.threeSum([])) == []

    print("all tests passed")
