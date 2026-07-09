# 方法1：暴力 pop 删除


class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        """
        暴力：遍历统计次数，超过 2 次就 pop。
        时间复杂度: O(n^2)
        空间复杂度: O(1)
        """
        if not nums:
            return 0

        i = 0
        count = 1

        while i < len(nums) - 1:
            if nums[i] == nums[i + 1]:
                count += 1
                if count > 2:
                    nums.pop(i + 1)
                else:
                    i += 1
            else:
                count = 1
                i += 1

        return len(nums)


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

    nums = []
    assert solver.removeDuplicates(nums) == 0


if __name__ == "__main__":
    run_test()
    print("all tests passed")
