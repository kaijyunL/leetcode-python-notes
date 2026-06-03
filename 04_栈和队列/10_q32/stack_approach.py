def longestValidParentheses(s: str) -> int:
    """
    栈解法：存储下标，利用参照物计算长度
    时间复杂度: O(n)
    空间复杂度: O(n)
    """
    max_ans = 0
    stack = [-1]  # 初始化参照物，代表上一个未匹配右括号的位置
    
    for i, char in enumerate(s):
        if char == '(':
            stack.append(i)  # 左括号下标入栈
        else:
            stack.pop()      # 尝试匹配
            if not stack:
                stack.append(i)  # 栈空说明此右括号无法匹配，设为新的参照物
            else:
                max_ans = max(max_ans, i - stack[-1])  # 计算当前有效长度
                
    return max_ans

if __name__ == "__main__":
    test_cases = ["(()", ")()())", "", "()(())"]
    for s in test_cases:
        print(f"Input: '{s}', Result: {longestValidParentheses(s)}")
