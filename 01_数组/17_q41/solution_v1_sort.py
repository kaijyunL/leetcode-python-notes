from typing import List

def firstMissingPositive(nums: List[int]) -> int:
    """
    方法一：排序法
    时间复杂度: O(N log N)
    空间复杂度: O(1) (取决于排序的空间复杂度)
    """
    # 1. 对数组进行排序
    nums.sort()
    
    # 2. 我们期望看到的正整数，初始为 1
    res = 1
    
    # 3. 遍历排序后的数组
    for num in nums:
        # 如果当前数字等于我们的期望值，说明找到了，期望值 + 1
        if num == res:
            res += 1
        # 如果当前数字大于期望值，由于数组已排序，说明期望值在数组中缺失
        elif num > res:
            return res
            
    # 4. 如果遍历完都没找到缺失的（或者数组为空/全是负数），则返回最后的期望值
    return res

# 测试代码
if __name__ == "__main__":
    test_cases = [
        ([1, 2, 0], 3),
        ([3, 4, -1, 1], 2),
        ([7, 8, 9, 11, 12], 1),
        ([], 1)
    ]
    
    for nums, expected in test_cases:
        result = firstMissingPositive(nums[:]) # 使用副本，防止修改原数组影响测试
        print(f"输入: {nums} -> 预期: {expected}, 实际: {result}, {'通过' if result == expected else '不通过'}")
