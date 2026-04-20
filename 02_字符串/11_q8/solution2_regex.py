import re

class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        # 匹配规则：以可选的正负号开头，后接一个或多个数字
        match = re.search(r'^[\+\-]?\d+', s)
        if not match:
            return 0
        
        # 提取匹配内容并转换
        res = int(match.group())
        
        # 边界处理
        INT_MAX, INT_MIN = 2**31 - 1, -2**31
        return max(INT_MIN, min(INT_MAX, res))

# 测试代码
if __name__ == "__main__":
    sol = Solution()
    print(sol.myAtoi("42"))            # 输出: 42
    print(sol.myAtoi("   -42"))         # 输出: -42
    print(sol.myAtoi("-91283472332"))   # 输出: -2147483648
