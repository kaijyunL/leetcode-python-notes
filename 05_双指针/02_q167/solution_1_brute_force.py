# 方法1：暴力枚举


class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        """
        暴力：枚举所有两两组合。
        时间复杂度: O(n^2)
        空间复杂度: O(1)
        """
        n = len(numbers)
        for i in range(n):
            for j in range(i + 1, n):
                if numbers[i] + numbers[j] == target:
                    return [i + 1, j + 1]
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
