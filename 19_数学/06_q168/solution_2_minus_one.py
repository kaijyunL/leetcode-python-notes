# 方法2：每次先 -1 再 divmod（面试主推）
# Excel 列号是“没有 0 的 26 进制”，每位取 1~26 而 % 26 只能得到 0~25，刚好差 1。
# 在每轮前先把 n 减 1，把 1~26 平移成 0~25，之后就是标准进制转换。
# 时间 O(log n)，空间 O(log n)


class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        chars = []
        n = columnNumber
        while n > 0:
            n -= 1
            chars.append(chr(n % 26 + ord("A")))
            n //= 26
        return "".join(reversed(chars))


if __name__ == "__main__":
    s = Solution()
    print(s.convertToTitle(1))           # "A"
    print(s.convertToTitle(26))          # "Z"
    print(s.convertToTitle(27))          # "AA"
    print(s.convertToTitle(28))          # "AB"
    print(s.convertToTitle(52))          # "AZ"
    print(s.convertToTitle(701))         # "ZY"
    print(s.convertToTitle(702))         # "ZZ"
    print(s.convertToTitle(703))         # "AAA"
    print(s.convertToTitle(2147483647))  # "FXSHRXW"
