class Solution:
    def isNumber(self, s: str) -> bool:
        states = [
            {'sign': 1, 'digit': 2, 'dot': 3},
            {'digit': 2, 'dot': 3},
            {'digit': 2, 'dot': 4, 'e': 6},
            {'digit': 5},
            {'digit': 5, 'e': 6},
            {'digit': 5, 'e': 6},
            {'sign': 7, 'digit': 8},
            {'digit': 8},
            {'digit': 8}
        ]
        
        current_state = 0
        
        for char in s:
            ctype = ''
            if char in '+-':
                ctype = 'sign'
            elif char in 'eE':
                ctype = 'e'
            elif char == '.':
                ctype = 'dot'
            elif char.isdigit():
                ctype = 'digit'
            else:
                return False
                
            if ctype not in states[current_state]:
                return False
                
            current_state = states[current_state][ctype]
            
        return current_state in {2, 4, 5, 8}

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
    
    print("\nDFA 有限状态自动机测试通过！")
