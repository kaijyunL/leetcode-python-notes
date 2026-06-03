from typing import List

def trap(height: List[int]) -> int:
    """
    暴力解法：时间复杂度 O(n^2), 空间复杂度 O(1)
    """
    n = len(height)
    ans = 0
    # 遍历每一列（去掉第一列和最后一列，因为它们接不到水）
    for i in range(1, n - 1):
        left_max = 0
        right_max = 0
        # 找左边最高
        for j in range(i, -1, -1):
            left_max = max(left_max, height[j])
        # 找右边最高
        for j in range(i, n):
            right_max = max(right_max, height[j])
        
        # 累加当前列的水量
        ans += min(left_max, right_max) - height[i]
    
    return ans

if __name__ == "__main__":
    test_case = [0,1,0,2,1,0,1,3,2,1,2,1]
    print(f"输入: {test_case}")
    print(f"输出: {trap(test_case)}")  # 期待输出: 6
