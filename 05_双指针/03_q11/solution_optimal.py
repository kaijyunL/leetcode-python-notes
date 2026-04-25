from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        最优解法：双指针
        时间复杂度: O(n)
        空间复杂度: O(1)
        """
        left, right = 0, len(height) - 1
        max_area = 0
        
        while left < right:
            # 计算当前面积
            # 宽为指针间距，高为两端点中较短的一方
            current_area = (right - left) * min(height[left], height[right])
            max_area = max(max_area, current_area)
            
            # 移动逻辑：始终移动较短的那一侧
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
                
        return max_area

# 测试代码
if __name__ == "__main__":
    sol = Solution()
    test_case = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    print(f"输入: {test_case}")
    print(f"最大水量 (最优解法): {sol.maxArea(test_case)}")
