# 方法3：Legendre 公式 / 按 5 的幂分层（面试主推）
# 答案 = n//5 + n//25 + n//125 + ...
# 实现上每轮把 n 替换成 n//5，连续除等价于一次除 5 的高次幂
# 时间 O(log_5 n)，空间 O(1)


class Solution:
    def trailingZeroes(self, n: int) -> int:
        count = 0
        while n > 0:
            n //= 5
            count += n
        return count


if __name__ == "__main__":
    s = Solution()
    print(s.trailingZeroes(0))     # 0
    print(s.trailingZeroes(3))     # 0
    print(s.trailingZeroes(5))     # 1
    print(s.trailingZeroes(10))    # 2
    print(s.trailingZeroes(25))    # 6
    print(s.trailingZeroes(30))    # 7
    print(s.trailingZeroes(100))   # 24
    print(s.trailingZeroes(125))   # 31
    print(s.trailingZeroes(10000)) # 2499
