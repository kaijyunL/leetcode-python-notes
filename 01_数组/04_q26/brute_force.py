from typing import List

def removeDuplicates(nums: List[int]) -> int:
    """
    暴力解法：使用额外空间存储唯一元素，再拷贝回原数组
    """
    if not nums:
        return 0
    
    # 1. 创建辅助空间存储唯一元素
    unique_nums = []
    for x in nums:
        # 由于数组有序，只需检查是否与最后一个加入的元素相同
        if not unique_nums or x != unique_nums[-1]:
            unique_nums.append(x)
    
    # 2. 将结果拷贝回原数组（题目要求原地修改）
    k = len(unique_nums)
    for i in range(k):
        nums[i] = unique_nums[i]
        
    return k

# 测试代码
if __name__ == "__main__":
    test_cases = [
        [1, 1, 2],
        [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    ]
    
    for nums in test_cases:
        print(f"原数组: {nums}")
        original_nums = nums.copy()
        k = removeDuplicates(nums)
        print(f"去重后长度: {k}")
        print(f"去重后的前k个元素: {nums[:k]}")
        print("-" * 20)
