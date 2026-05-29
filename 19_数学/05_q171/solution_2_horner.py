# 方法2：从左到右秦九韶式累乘（面试主推）
# 把 Excel 列号理解成“没有 0 的 26 进制”，每读一位就把已有结果 * 26 再加上新位
# 时间 O(n)，空间 O(1)


class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        ans = 0
        for ch in columnTitle:
            ans = ans * 26 + (ord(ch) - ord("A") + 1)
        return ans


if __name__ == "__main__":
    s = Solution()
    print(s.titleToNumber("A"))        # 1
    print(s.titleToNumber("AB"))       # 28
    print(s.titleToNumber("ZY"))       # 701
    print(s.titleToNumber("FXSHRXW"))  # 2147483647
