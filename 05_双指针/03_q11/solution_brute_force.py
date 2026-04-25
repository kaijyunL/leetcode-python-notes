from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        暴力解法：枚举所有可能的组合
        时间复杂度: O(n^2)
        空间复杂度: O(1)
        """
        max_area = 0
        n = len(height)
        for i in range(n):
            for j in range(i + 1, n):
                # 计算当前面积：宽 * 最小高度
                current_area = (j - i) * min(height[i], height[j])
                max_area = max(max_area, current_area)
        return max_area

# 测试代码
if __name__ == "__main__":
    sol = Solution()
    test_case = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    print(f"输入: {test_case}")
    print(f"最大水量 (暴力解法): {sol.maxArea(test_case)}")
