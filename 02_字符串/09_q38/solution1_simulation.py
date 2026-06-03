class Solution:
    def countAndSay(self, n: int) -> str:
        res = "1"
        
        for _ in range(2, n + 1):
            parts = []
            i = 0
            
            while i < len(res):
                count = 1
                while i + 1 < len(res) and res[i] == res[i + 1]:
                    count += 1
                    i += 1
                    
                parts.append(str(count) + res[i])
                i += 1
                
            res = ''.join(parts)
            
        return res

if __name__ == "__main__":
    solution = Solution()
    print(solution.countAndSay(1))
    print(solution.countAndSay(4))
    print(solution.countAndSay(5))
