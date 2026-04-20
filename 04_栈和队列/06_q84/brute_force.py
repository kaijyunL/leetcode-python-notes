def largestRectangleArea(heights):
    """
    暴力解法：枚举高度 (中心扩散)
    时间复杂度: O(n^2)
    空间复杂度: O(1)
    """
    n = len(heights)
    max_area = 0
    
    for i in range(n):
        height = heights[i]
        left = i
        right = i
        
        # 向左寻找第一个比当前矮的
        while left >= 0 and heights[left] >= height:
            left -= 1
        
        # 向右寻找第一个比当前矮的
        while right < n and heights[right] >= height:
            right += 1
            
        # 宽度 = (right - 1) - (left + 1) + 1 = right - left - 1
        width = right - left - 1
        max_area = max(max_area, width * height)
        
    return max_area

# 测试代码
if __name__ == "__main__":
    test_cases = [
        ([2, 1, 5, 6, 2, 3], 10),
        ([2, 4], 4),
        ([1, 1], 2)
    ]
    for h, expected in test_cases:
        res = largestRectangleArea(h)
        print(f"Heights: {h}, Expected: {expected}, Got: {res}")
