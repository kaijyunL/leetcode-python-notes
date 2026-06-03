class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        
        m, n = len(num1), len(num2)
        res = [0] * (m + n)
        
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                mul = int(num1[i]) * int(num2[j])
                p1, p2 = i + j, i + j + 1
                total = mul + res[p2]
                res[p2] = total % 10
                res[p1] += total // 10
                
        start_idx = 0
        while start_idx < len(res) and res[start_idx] == 0:
            start_idx += 1
            
        ans = [str(x) for x in res[start_idx:]]
        return "".join(ans)

if __name__ == "__main__":
    solution = Solution()
    print('123 * 456 =', solution.multiply("123", "456"))
    print('2 * 3 =', solution.multiply("2", "3"))

