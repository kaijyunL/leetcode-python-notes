def is_valid_optimal(s: str) -> bool:
    if len(s) % 2 != 0:
        return False
        
    stack = []
    mapping = {")": "(", "]": "[", "}": "{"}
    
    for char in s:
        if char in mapping:
            # 弹栈并检查匹配
            top_element = stack.pop() if stack else '#'
            if mapping[char] != top_element:
                return False
        else:
            stack.append(char)
            
    return not stack

if __name__ == "__main__":
    test_cases = ["()", "()[]{}", "(]", "([)]", "{[]}"]
    for test in test_cases:
        print(f"输入: {test}, 结果: {is_valid_optimal(test)}")
