def longestValidParentheses(s: str) -> int:
    """
    双计数器/贪心解法：正向反向各遍历一次
    时间复杂度: O(n)
    空间复杂度: O(1)
    """
    left, right, max_ans = 0, 0, 0
    
    # 正向遍历
    for char in s:
        if char == '(':
            left += 1
        else:
            right += 1
        if left == right:
            max_ans = max(max_ans, 2 * right)
        elif right > left:
            left = right = 0
            
    # 反向遍历，处理像 "((()" 这种左括号过多的情况
    left = right = 0
    for char in reversed(s):
        if char == '(':
            left += 1
        else:
            right += 1
        if left == right:
            max_ans = max(max_ans, 2 * left)
        elif left > right:
            left = right = 0
            
    return max_ans

if __name__ == "__main__":
    test_cases = ["(()", ")()())", "", "()(())"]
    for s in test_cases:
        print(f"Input: '{s}', Result: {longestValidParentheses(s)}")
