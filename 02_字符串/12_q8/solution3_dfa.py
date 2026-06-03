class Automaton:
    def __init__(self):
        self.state = 'start'
        self.sign = 1
        self.ans = 0
        # 状态转移表
        self.table = {
            'start': ['start', 'signed', 'in_number', 'end'],
            'signed': ['end', 'end', 'in_number', 'end'],
            'in_number': ['end', 'end', 'in_number', 'end'],
            'end': ['end', 'end', 'end', 'end'],
        }

    def get_col(self, c):
        if c.isspace(): return 0
        if c in ('+', '-'): return 1
        if c.isdigit(): return 2
        return 3

    def get(self, c):
        self.state = self.table[self.state][self.get_col(c)]
        if self.state == 'in_number':
            self.ans = self.ans * 10 + int(c)
            # 及时截断
            self.ans = min(self.ans, 2**31 - 1 if self.sign == 1 else 2**31)
        elif self.state == 'signed':
            self.sign = 1 if c == '+' else -1

class Solution:
    def myAtoi(self, s: str) -> int:
        automaton = Automaton()
        for c in s:
            automaton.get(c)
            if automaton.state == 'end':
                break
        return automaton.sign * automaton.ans

# 测试代码
if __name__ == "__main__":
    sol = Solution()
    print(sol.myAtoi("   -42"))         # 输出: -42
    print(sol.myAtoi("4193 with words"))# 输出: 4193
    print(sol.myAtoi("2147483648"))     # 输出: 2147483647
