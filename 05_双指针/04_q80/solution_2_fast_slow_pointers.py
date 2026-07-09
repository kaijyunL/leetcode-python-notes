# 方法2：快慢指针覆盖写（面试主推）


class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        """
        快慢指针：和 slow-2 比，允许保留 2 次。
        时间复杂度: O(n)
        空间复杂度: O(1)
        """
        if len(nums) <= 2:
            return len(nums)

        slow = 2

        for fast in range(2, len(nums)):
            if nums[fast] != nums[slow - 2]:
                nums[slow] = nums[fast]
                slow += 1

        return slow


def run_test() -> None:
    solver = Solution()

    nums = [1, 1, 1, 2, 2, 3]
    assert solver.removeDuplicates(nums) == 5
    assert nums[:5] == [1, 1, 2, 2, 3]

    nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]
    assert solver.removeDuplicates(nums) == 7
    assert nums[:7] == [0, 0, 1, 1, 2, 3, 3]

    nums = [1, 1, 1]
    assert solver.removeDuplicates(nums) == 2
    assert nums[:2] == [1, 1]

    nums = [1, 2, 3]
    assert solver.removeDuplicates(nums) == 3

    nums = [1, 1]
    assert solver.removeDuplicates(nums) == 2


if __name__ == "__main__":
    run_test()
    print("all tests passed")
