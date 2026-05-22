class Solution:
    def romanToInt(self, s: str) -> int:
        """
        :type s: str
        :rtype: int
        """
        # 1. 建立罗马数字与整数的映射关系
        roman_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        total = 0
        n = len(s)
        
        # 2. 遍历字符串
        for i in range(n):
            value = roman_map[s[i]]
            
            # 3. 核心判断：如果当前值小于下一个值，说明是减法情况（如 IV = 5-1）
            # 注意边界条件：i < n - 1 确保不会访问越界
            if i < n - 1 and value < roman_map[s[i + 1]]:
                total -= value
            else:
                total += value
                
        return total

# 测试样例
if __name__ == "__main__":
    sol = Solution()
    print(f"III -> {sol.romanToInt('III')}")      # 输出: 3
    print(f"IV -> {sol.romanToInt('IV')}")        # 输出: 4
    print(f"IX -> {sol.romanToInt('IX')}")        # 输出: 9
    print(f"LVIII -> {sol.romanToInt('LVIII')}")  # 输出: 58
    print(f"MCMXCIV -> {sol.romanToInt('MCMXCIV')}") # 输出: 1994
