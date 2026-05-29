# 方法1：直接套 26 进制（踩坑版，结果是错的，仅用于对比）
# % 26 永远拿不到 26，n=26、52、702 等临界值都会翻车


class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        chars = []
        n = columnNumber
        while n > 0:
            digit = n % 26
            # digit 期望落在 1~26，但实际是 0~25，0 的时候字母会越界
            chars.append(chr(digit - 1 + ord("A")))
            n //= 26
        return "".join(reversed(chars))


if __name__ == "__main__":
    s = Solution()
    # 1 -> "A" (碰巧能过)
    print(s.convertToTitle(1))
    # 26 -> 期望 "Z"，实际会得到非字母（'@' 之类）
    print(repr(s.convertToTitle(26)))
    # 52 -> 期望 "AZ"，实际会算错
    print(repr(s.convertToTitle(52)))
