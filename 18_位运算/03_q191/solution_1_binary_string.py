# 方法1：二进制字符串统计


class Solution:
    def hammingWeight(self, n: int) -> int:
        binary = bin(n)[2:]
        ans = 0

        for ch in binary:
            if ch == "1":
                ans += 1

        return ans


if __name__ == "__main__":
    solver = Solution()
    test_cases = [11, 128, 0, 7]

    for n in test_cases:
        print(f"n={n}, answer={solver.hammingWeight(n)}")
