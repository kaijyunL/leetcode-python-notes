# 方法2：二分查找


class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        """
        固定一个数，二分找另一个。
        时间复杂度: O(n log n)
        空间复杂度: O(1)
        """
        n = len(numbers)
        for i in range(n):
            complement = target - numbers[i]
            lo, hi = i + 1, n - 1

            while lo <= hi:
                mid = (lo + hi) // 2
                if numbers[mid] == complement:
                    return [i + 1, mid + 1]
                elif numbers[mid] < complement:
                    lo = mid + 1
                else:
                    hi = mid - 1

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
