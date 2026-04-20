from typing import List

def trap(height: List[int]) -> int:
    """
    双指针解法（最优解）：时间复杂度 O(n), 空间复杂度 O(1)
    """
    if not height:
        return 0
    
    left, right = 0, len(height) - 1
    left_max, right_max = 0, 0
    ans = 0
    
    while left < right:
        # 更新当前的左右峰值
        left_max = max(left_max, height[left])
        right_max = max(right_max, height[right])
        
        # 核心逻辑：哪边短就处理哪边
        # 只要 left_max < right_max，left 指针处的出水高度就由 left_max 决定
        if left_max < right_max:
            ans += left_max - height[left]
            left += 1
        else:
            ans += right_max - height[right]
            right -= 1
            
    return ans

if __name__ == "__main__":
    test_case = [0,1,0,2,1,0,1,3,2,1,2,1]
    print(f"输入: {test_case}")
    print(f"输出: {trap(test_case)}")  # 期待输出: 6
