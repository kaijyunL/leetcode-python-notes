# 方法1：逐个数字单独统计


class Solution:
    def countBits(self, n: int) -> list[int]:
        def count_ones(num: int) -> int:
            count = 0
            while num:
                num &= num - 1
                count += 1
            return count

        ans = []
        for num in range(n + 1):
            ans.append(count_ones(num))
        return ans


if __name__ == "__main__":
    solver = Solution()
    test_cases = {
        0: [0],
        2: [0, 1, 1],
        5: [0, 1, 1, 2, 1, 2],
        8: [0, 1, 1, 2, 1, 2, 2, 3, 1],
    }

    for n, expected in test_cases.items():
        assert solver.countBits(n) == expected

    print("all tests passed")
