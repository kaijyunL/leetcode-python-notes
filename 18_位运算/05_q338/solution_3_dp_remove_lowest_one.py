# 方法3：DP + 去掉最右边的 1


class Solution:
    def countBits(self, n: int) -> list[int]:
        ans = [0] * (n + 1)

        for i in range(1, n + 1):
            ans[i] = ans[i & (i - 1)] + 1

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
