class Solution:
    def isNumber(self, s: str) -> bool:
        has_digit = False
        has_dot = False
        has_e = False
        
        for i, char in enumerate(s):
            if char.isdigit():
                has_digit = True
            elif char in ('+', '-'):
                if i > 0 and s[i-1] not in ('e', 'E'):
                    return False
            elif char == '.':
                if has_dot or has_e:
                    return False
                has_dot = True
            elif char in ('e', 'E'):
                if has_e or not has_digit:
                    return False
                has_e = True
                has_digit = False
            else:
                return False
                
        return has_digit

# --- 测试用例 ---
if __name__ == "__main__":
    test_cases = ["2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789"]
    false_cases = ["abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53", "."]
    
    sol = Solution()
    print("=== True Cases ===")
    for case in test_cases:
        assert sol.isNumber(case) == True, f"Failed on {case}"
        print(f"'{case}' -> True")
        
    print("\n=== False Cases ===")
    for case in false_cases:
        assert sol.isNumber(case) == False, f"Failed on {case}"
        print(f"'{case}' -> False")
    
    print("\n标志位循环遍历测试通过！")
