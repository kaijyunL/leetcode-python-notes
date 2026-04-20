from typing import List

def firstMissingPositive(nums: List[int]) -> int:
    """
    方法三：置换法 (原地哈希) - 最优解
    时间复杂度: O(N)
    空间复杂度: O(1)
    """
    n = len(nums)
    
    # 1. 置换：将数字 x 移动到下标 x-1 的位置上
    # 例如：1 放到 nums[0], 2 放到 nums[1]...
    for i in range(n):
        # 只要 nums[i] 是一个在 [1, n] 范围内的正整数，
        # 且它目前所在的位置不正确（即 nums[i] != nums[nums[i]-1]），则不断交换
        # 注意：这里使用 while 是因为交换过来的数可能也需要继续交换
        while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
            # Python 特有的交换写法：nums[i], nums[nums[i]-1] = nums[nums[i]-1], nums[i]
            # 这里要注意，nums[i]-1 这个下标依赖于 nums[i] 的变化，
            # 这种多元赋值在 Python 中是从左往右求出的，有时会产生意外风险。
            # 为了严谨起见，我们手动记录下标：
            target_idx = nums[i] - 1
            nums[i], nums[target_idx] = nums[target_idx], nums[i]
            
    # 2. 第二次遍历找出缺失的数
    # 如果位置 i+1 不等于 nums[i]，说明 i+1 缺失
    for i in range(n):
        if nums[i] != i + 1:
            return i + 1
            
    # 3. 如果所有位置都匹配，说明缺失的是接在结尾后的正数 n + 1
    return n + 1

# 测试代码
if __name__ == "__main__":
    test_cases = [
        ([1, 2, 0], 3),
        ([3, 4, -1, 1], 2),
        ([7, 8, 9, 11, 12], 1),
        ([1, 2, 3, 4], 5)
    ]
    
    for nums, expected in test_cases:
        # 置换法会修改原数组，因此传入时拷贝一个副本，便于演示输入输出
        original_nums = nums[:]
        result = firstMissingPositive(nums)
        print(f"输入: {original_nums} -> 预期: {expected}, 实际: {result}, {'通过' if result == expected else '不通过'}")
