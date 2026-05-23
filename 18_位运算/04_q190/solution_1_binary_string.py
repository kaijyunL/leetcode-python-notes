# 方法1：字符串反转


class Solution:
    def reverseBits(self, n: int) -> int:
        bits = bin(n)[2:].zfill(32)
        reversed_bits = bits[::-1]
        return int(reversed_bits, 2)


if __name__ == "__main__":
    solver = Solution()
    test_cases = [43261596, 4294967293, 1, 0]

    for n in test_cases:
        print(f"n={n}, answer={solver.reverseBits(n)}")
