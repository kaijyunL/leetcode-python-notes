class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        
        n = len(s)
        t = numRows * 2 - 2
        c = (n + t - 1) // t * (numRows - 1)
        
        mat = [[''] * c for _ in range(numRows)]
        
        x, y = 0, 0
        for i, ch in enumerate(s):
            mat[x][y] = ch
            if i % t < numRows - 1:
                x += 1
            else:
                x -= 1
                y += 1
                
        res = []
        for row in mat:
            for ch in row:
                if ch:
                    res.append(ch)
        return ''.join(res)

if __name__ == "__main__":
    sol = Solution()
    print("解法一：二维矩阵模拟")
    print("测试输入: s = 'PAYPALISHIRING', numRows = 3")
    print("期望输出: PAHNAPLSIIGYIR")
    print("实际输出:", sol.convert("PAYPALISHIRING", 3))
