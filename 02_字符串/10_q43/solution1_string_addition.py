class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        def addStrings(s1: str, s2: str) -> str:
            res = []
            i, j = len(s1) - 1, len(s2) - 1
            carry = 0
            while i >= 0 or j >= 0 or carry:
                x = int(s1[i]) if i >= 0 else 0
                y = int(s2[j]) if j >= 0 else 0
                total = x + y + carry
                carry = total // 10
                res.append(str(total % 10))
                i -= 1
                j -= 1
            return "".join(res[::-1])

        ans = "0"
        
        for j in range(len(num2) - 1, -1, -1):
            curr_res = []
            carry = 0
            
            for _ in range(len(num2) - 1 - j):
                curr_res.append("0")
                
            y = int(num2[j])
            
            for i in range(len(num1) - 1, -1, -1):
                x = int(num1[i])
                product = x * y + carry
                curr_res.append(str(product % 10))
                carry = product // 10
                
            if carry > 0:
                curr_res.append(str(carry))
                
            curr_res = "".join(curr_res[::-1])
            ans = addStrings(ans, curr_res)

        return ans

if __name__ == "__main__":
    solution = Solution()
    print('123 * 456 =', solution.multiply("123", "456"))
    print('2 * 3 =', solution.multiply("2", "3"))

