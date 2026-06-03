from typing import List

def dailyTemperatures(temperatures: List[int]) -> List[int]:
    """
    最优解法：单调栈
    时间复杂度: O(n)
    空间复杂度: O(n)
    """
    n = len(temperatures)
    ans = [0] * n
    stack = []  # 存储下标
    
    for i in range(n):
        # 当栈不为空，且当前温度大于栈顶温度时
        while stack and temperatures[i] > temperatures[stack[-1]]:
            prev_index = stack.pop()
            ans[prev_index] = i - prev_index
        # 将当前下标入栈，等待它的更高温
        stack.append(i)
        
    return ans

if __name__ == "__main__":
    test_data = [73, 74, 75, 71, 69, 72, 76, 73]
    print(f"输入: {test_data}")
    print(f"输出: {dailyTemperatures(test_data)}")
