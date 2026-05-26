# 方法3：公式生成


class Solution:
    def grayCode(self, n: int) -> list[int]:
        return [i ^ (i >> 1) for i in range(1 << n)]


def is_valid_gray_code(nums: list[int], n: int) -> bool:
    if len(nums) != 1 << n or nums[0] != 0 or len(set(nums)) != len(nums):
        return False

    def differs_by_one_bit(x: int, y: int) -> bool:
        diff = x ^ y
        return diff != 0 and (diff & (diff - 1)) == 0

    for i in range(1, len(nums)):
        if not differs_by_one_bit(nums[i - 1], nums[i]):
            return False
    return n == 0 or differs_by_one_bit(nums[-1], nums[0])


if __name__ == "__main__":
    solver = Solution()

    assert solver.grayCode(0) == [0]
    assert solver.grayCode(1) == [0, 1]
    assert solver.grayCode(2) == [0, 1, 3, 2]

    for n in range(6):
        assert is_valid_gray_code(solver.grayCode(n), n)

    print("all tests passed")
