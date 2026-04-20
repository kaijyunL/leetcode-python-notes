class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
            
        n = len(s)
        t = numRows * 2 - 2  
        res = []
        
        for i in range(numRows):
            for j in range(0, n - i, t):
                res.append(s[j + i])
                if 0 < i < numRows - 1 and j + t - i < n:
                    res.append(s[j + t - i])
                    
        return "".join(res)

if __name__ == "__main__":
    sol = Solution()
    print("解法三：直接构造数学规律代码")
    print("测试输入: s = 'PAYPALISHIRING', numRows = 4")
    print("期望输出: PINALSIGYAHRPI")
    print("实际输出:", sol.convert("PAYPALISHIRING", 4))
