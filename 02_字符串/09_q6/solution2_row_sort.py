class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
            
        rows = [''] * numRows
        i, flag = 0, -1
        
        for ch in s:
            rows[i] += ch
            if i == 0 or i == numRows - 1:
                flag = -flag
            i += flag
            
        return "".join(rows)

if __name__ == "__main__":
    sol = Solution()
    print("解法二：按行排序 (大幅优化空间)")
    print("测试输入: s = 'PAYPALISHIRING', numRows = 4")
    print("期望输出: PINALSIGYAHRPI")
    print("实际输出:", sol.convert("PAYPALISHIRING", 4))
