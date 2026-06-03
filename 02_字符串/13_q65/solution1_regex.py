import re

class Solution:
    def isNumber(self, s: str) -> bool:
        pattern = r"^[+-]?(\d+\.\d*|\.\d+|\d+)([eE][+-]?\d+)?$"
        return bool(re.match(pattern, s))

# --- 测试用例 ---
if __name__ == "__main__":
    test_cases = ["2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789"]
    false_cases = ["abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"]
    
    sol = Solution()
    print("=== True Cases ===")
    for case in test_cases:
        assert sol.isNumber(case) == True, f"Failed on {case}"
        print(f"'{case}' -> True")
        
    print("\n=== False Cases ===")
    for case in false_cases:
        assert sol.isNumber(case) == False, f"Failed on {case}"
        print(f"'{case}' -> False")
    
    print("\n正则测试通过！")
