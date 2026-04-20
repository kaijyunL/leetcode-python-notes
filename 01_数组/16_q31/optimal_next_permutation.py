from typing import List

def next_permutation(nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    
    解法二：最优解 - 两遍扫描法 (Two-pass Path)
    时间复杂度 $O(n)$，空间复杂度 $O(1)$。
    """
    n = len(nums)
    if n <= 1:
        return
    
    # 步骤 1：寻找转折点 (i)
    # 从右往左寻找第一对相邻升序 (i, i+1)，满足 nums[i] < nums[i+1]
    i = n - 2
    while i >= 0 and nums[i] >= nums[i+1]:
        i -= 1
        
    # 如果找到了转折点 i (i >= 0)
    if i >= 0:
        # 步骤 2：在该转折点右侧寻找略大的数 (j)
        # 再次从右往左寻找第一个满足 nums[j] > nums[i] 的数
        j = n - 1
        while j >= 0 and nums[j] <= nums[i]:
            j -= 1
            
        # 步骤 3：交换 nums[i] 和 nums[j]
        nums[i], nums[j] = nums[j], nums[i]
        
    # 步骤 4：反转 nums[i+1] 到 nums[n-1] 之间的所有数字
    # 这一步是为了让修改后的部分保持升序排列，使“下一个排列”增幅最小。
    # 如果 i = -1 (即整个数组原先正序) 这步也会反转数组为升序排列。
    left, right = i + 1, n - 1
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1

# 测试用例
if __name__ == "__main__":
    example1 = [1, 2, 3]
    next_permutation(example1)
    print(f"输入: [1, 2, 3] -> 输出: {example1}") # 期望: [1, 3, 2]

    example2 = [3, 2, 1]
    next_permutation(example2)
    print(f"输入: [3, 2, 1] -> 输出: {example2}") # 期望: [1, 2, 3]

    example3 = [1, 1, 5]
    next_permutation(example3)
    print(f"输入: [1, 1, 5] -> 输出: {example3}") # 期望: [1, 5, 1]
    
    example4 = [1, 5, 8, 4, 7, 6, 5, 3, 1]
    next_permutation(example4)
    print(f"输入: [1, 5, 8, 4, 7, 6, 5, 3, 1] -> 输出: {example4}") # 期望: [1, 5, 8, 5, 1, 3, 4, 6, 7]
