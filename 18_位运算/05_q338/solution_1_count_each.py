# 方法1：逐个数字单独统计


class Solution:
    def countBits(self, n: int) -> list[int]:
        def count_ones(num):
            ans = 0
            while num:
                num &= num - 1
                ans += 1
            return ans

        ans = []
        for num in range(n + 1):
            ans.append(count_ones(num))
        return ans


if __name__ == "__main__":
    solver = Solution()
    test_cases = [2, 5, 0, 8]

    for n in test_cases:
        print(f"n={n}, answer={solver.countBits(n)}")
