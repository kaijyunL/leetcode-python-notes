def largestRectangleArea(heights):
    """
    最优解法：单调栈 (Monotonic Stack)
    时间复杂度: O(n)
    空间复杂度: O(n)
    """
    # 技巧：首尾添加哨兵 0，简化逻辑
    heights = [0] + heights + [0]
    stack = []
    max_area = 0
    
    for i in range(len(heights)):
        # 当遇到当前高度比栈顶高度矮时，说明栈顶元素的右边界找到了
        while stack and heights[i] < heights[stack[-1]]:
            # 弹出栈顶作为矩形的高度
            h_idx = stack.pop()
            h = heights[h_idx]
            
            # 弹出后的栈顶就是矩形的左边界 (第一个比它矮的)
            # 宽度 = 右边界索引 i - 左边界索引 - 1
            w = i - stack[-1] - 1
            
            max_area = max(max_area, w * h)
            
        # 否则，当前索引入栈，继续保持栈内高度单调递增
        stack.append(i)
        
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
