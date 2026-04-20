from typing import List

def majority_element_brute_force(nums: List[int]) -> int:
    """
    暴力解法：遍历数组中的每个数，统计其出现的频率。
    时间复杂度: O(n^2)
    空间复杂度: O(1)
    """
    n = len(nums)
    # 多数元素出现的阈值
    majority_count = n // 2
    
    for i in range(n):
        count = 0
        # 统计 nums[i] 在数组中出现的总次数
        for j in range(n):
            if nums[j] == nums[i]:
                count += 1
        
        # 如果次数超过 n // 2，则返回该元素
        if count > majority_count:
            return nums[i]

# 测试代码
if __name__ == "__main__":
    test_nums = [2, 2, 1, 1, 1, 2, 2]
    print(f"输入: {test_nums}")
    print(f"多数元素 (暴力解法): {majority_element_brute_force(test_nums)}")
