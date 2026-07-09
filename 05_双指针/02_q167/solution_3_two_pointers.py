# 方法3：对撞双指针（面试主推）


class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        """
        对撞双指针：小了挪左换大的，大了挪右换小的。
        时间复杂度: O(n)
        空间复杂度: O(1)
        """
        left, right = 0, len(numbers) - 1

        while left < right:
            s = numbers[left] + numbers[right]
            if s == target:
                return [left + 1, right + 1]
            elif s < target:
                left += 1
            else:
                right -= 1

        return []


def run_test() -> None:
    solver = Solution()

    assert solver.twoSum([2, 7, 11, 15], 9) == [1, 2]
    assert solver.twoSum([2, 3, 4], 6) == [1, 3]
    assert solver.twoSum([-1, 0], -1) == [1, 2]
    assert solver.twoSum([1, 2, 3, 4, 5], 9) == [4, 5]
    assert solver.twoSum([0, 0, 3, 4], 0) == [1, 2]


if __name__ == "__main__":
    run_test()
    print("all tests passed")
