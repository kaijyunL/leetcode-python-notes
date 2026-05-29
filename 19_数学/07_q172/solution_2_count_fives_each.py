# 方法2：枚举每个 5 的倍数，数它含几个因子 5
# 不再算 n!，但仍是 O(n) 量级
# 时间 O(n)，空间 O(1)


class Solution:
    def trailingZeroes(self, n: int) -> int:
        count = 0
        for i in range(5, n + 1, 5):
            x = i
            while x % 5 == 0:
                count += 1
                x //= 5
        return count


if __name__ == "__main__":
    s = Solution()
    print(s.trailingZeroes(0))    # 0
    print(s.trailingZeroes(3))    # 0
    print(s.trailingZeroes(5))    # 1
    print(s.trailingZeroes(10))   # 2
    print(s.trailingZeroes(25))   # 6
    print(s.trailingZeroes(30))   # 7
    print(s.trailingZeroes(100))  # 24
