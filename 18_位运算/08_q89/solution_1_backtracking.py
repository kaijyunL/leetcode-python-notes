# 方法1：回溯尝试翻转一位


class Solution:
    def grayCode(self, n: int) -> list[int]:
        total = 1 << n
        path = [0]
        visited = {0}

        def differs_by_one_bit(x: int, y: int) -> bool:
            diff = x ^ y
            return diff != 0 and (diff & (diff - 1)) == 0

        def backtrack(cur: int) -> bool:
            if len(path) == total:
                return n == 0 or differs_by_one_bit(path[-1], path[0])

            for bit in range(n):
                nxt = cur ^ (1 << bit)
                if nxt in visited:
                    continue

                visited.add(nxt)
                path.append(nxt)

                if backtrack(nxt):
                    return True

                path.pop()
                visited.remove(nxt)

            return False

        backtrack(0)
        return path


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

    for n in range(4):
        assert is_valid_gray_code(solver.grayCode(n), n)

    print("all tests passed")
