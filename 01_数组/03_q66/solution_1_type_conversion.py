# 方法1：类型转换

from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        number = int("".join(str(digit) for digit in digits)) + 1
        return [int(digit) for digit in str(number)]


if __name__ == "__main__":
    solution = Solution()

    assert solution.plusOne([1, 2, 3]) == [1, 2, 4]
    assert solution.plusOne([4, 3, 2, 1]) == [4, 3, 2, 2]
    assert solution.plusOne([9]) == [1, 0]
    assert solution.plusOne([9, 9, 9]) == [1, 0, 0, 0]

    print("all tests passed")
