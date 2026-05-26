# 方法2：镜像构造


class Solution:
    def grayCode(self, n: int) -> list[int]:
        res = [0]
        head = 1

        for _ in range(n):
            for j in range(len(res) - 1, -1, -1):
                res.append(head + res[j])
            head <<= 1

        return res


# 以下是本地测试辅助，LeetCode 提交时不需要写。
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

    for n in range(5):
        assert is_valid_gray_code(solver.grayCode(n), n)

    print("all tests passed")
