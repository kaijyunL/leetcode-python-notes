# 方法1：从右往左累加，显式计算 26 的幂
# 时间 O(n)，空间 O(1)


class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        ans = 0
        power = 1

        for ch in reversed(columnTitle):
            digit = ord(ch) - ord("A") + 1
            ans += digit * power
            power *= 26

        return ans


if __name__ == "__main__":
    s = Solution()
    print(s.titleToNumber("A"))        # 1
    print(s.titleToNumber("AB"))       # 28
    print(s.titleToNumber("ZY"))       # 701
    print(s.titleToNumber("FXSHRXW"))  # 2147483647
