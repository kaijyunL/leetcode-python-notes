# 方法2：逐位取出并构造答案


class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0

        for _ in range(32):
            ans = (ans << 1) | (n & 1)
            n >>= 1

        return ans


if __name__ == "__main__":
    solver = Solution()
    test_cases = [43261596, 4294967293, 1, 0]

    for n in test_cases:
        print(f"n={n}, answer={solver.reverseBits(n)}")
