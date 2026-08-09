# 方法3：一趟三指针（荷兰国旗，面试主推）


class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        方法3：一趟三指针（荷兰国旗，面试主推）
        时间复杂度：O(n)
        空间复杂度：O(1)
        """
        zero = 0
        current = 0
        two = len(nums) - 1

        while current <= two:
            if nums[current] == 0:
                nums[zero], nums[current] = nums[current], nums[zero]
                zero += 1
                current += 1
            elif nums[current] == 2:
                nums[current], nums[two] = nums[two], nums[current]
                two -= 1
            else:
                current += 1


if __name__ == "__main__":
    solution = Solution()

    nums = [2, 0, 2, 1, 1, 0]
    solution.sortColors(nums)
    assert nums == [0, 0, 1, 1, 2, 2]

    nums = [2, 0, 1]
    solution.sortColors(nums)
    assert nums == [0, 1, 2]

    nums = [2, 2, 1, 1, 0, 0]
    solution.sortColors(nums)
    assert nums == [0, 0, 1, 1, 2, 2]

    nums = [0, 0, 0]
    solution.sortColors(nums)
    assert nums == [0, 0, 0]

    nums = [2, 2, 2]
    solution.sortColors(nums)
    assert nums == [2, 2, 2]

    print("all tests passed")
