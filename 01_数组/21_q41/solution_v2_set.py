from typing import List

def firstMissingPositive(nums: List[int]) -> int:
    """
    方法二：哈希表法
    时间复杂度: O(N)
    空间复杂度: O(N)
    """
    # 1. 把所有数存入哈希集合，查找时间为 O(1)
    num_set = set(nums)
    
    # 2. 从正整数 1 开始逐个检查
    res = 1
    # 最多检查 n + 1 次，因为缺失的第一个正数一定在 [1, n+1] 范围内
    while res in num_set:
        res += 1
        
    # 3. 第一个不在集合中的 res 即为答案
    return res

# 测试代码
if __name__ == "__main__":
    test_cases = [
        ([1, 2, 0], 3),
        ([3, 4, -1, 1], 2),
        ([7, 8, 9, 11, 12], 1)
    ]
    
    for nums, expected in test_cases:
        result = firstMissingPositive(nums)
        print(f"输入: {nums} -> 预期: {expected}, 实际: {result}, {'通过' if result == expected else '不通过'}")
