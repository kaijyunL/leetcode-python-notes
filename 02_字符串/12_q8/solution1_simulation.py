class Solution:
    def myAtoi(self, s: str) -> int:
        # 1. 处理前导空格
        s = s.lstrip()
        if not s:
            return 0
        
        # 2. 初始化变量
        res, i, sign = 0, 0, 1
        INT_MAX, INT_MIN = 2**31 - 1, -2**31

        # 3. 处理符号位
        if s[0] == '-':
            sign = -1
            i = 1
        elif s[0] == '+':
            i = 1

        # 4. 遍历数字并执行转换
        while i < len(s) and s[i].isdigit():
            res = res * 10 + int(s[i])
            i += 1
            
            # 实时检查是否越界（模拟 32 位环境）
            if sign * res > INT_MAX: return INT_MAX
            if sign * res < INT_MIN: return INT_MIN

        # 5. 返回带符号结果
        return sign * res

# 测试
if __name__ == "__main__":
    sol = Solution()
    test_cases = ["42", "   -42", "4193 with words", "words and 987", "-91283472332"]
    for test in test_cases:
        print(f"输入: '{test}' -> 输出: {sol.myAtoi(test)}")
