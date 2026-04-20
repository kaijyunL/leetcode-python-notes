from typing import List

def trap(height: List[int]) -> int:
    """
    动态规划解法：时间复杂度 O(n), 空间复杂度 O(n)
    """
    if not height:
        return 0
    
    n = len(height)
    left_max = [0] * n
    right_max = [0] * n
    
    # 预处理左侧最高
    left_max[0] = height[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i - 1], height[i])
        
    # 预处理右侧最高
    right_max[n - 1] = height[n - 1]
    for i in range(n - 2, -1, -1):
        right_max[i] = max(right_max[i + 1], height[i])
        
    # 计算总量
    ans = 0
    for i in range(n):
        ans += min(left_max[i], right_max[i]) - height[i]
        
    return ans

if __name__ == "__main__":
    test_case = [0,1,0,2,1,0,1,3,2,1,2,1]
    print(f"输入: {test_case}")
    print(f"输出: {trap(test_case)}")  # 期待输出: 6
