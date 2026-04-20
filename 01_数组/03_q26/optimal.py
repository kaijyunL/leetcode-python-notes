from typing import List

def removeDuplicates(nums: List[int]) -> int:
    """
    最优解法：双指针法 (Two Pointers)
    时间复杂度: O(n)
    空间复杂度: O(1)
    """
    if not nums:
        return 0
    
    # slow 指针指向当前确定不重复的序列末尾
    slow = 0
    
    # fast 指针用于向后扫描
    for fast in range(1, len(nums)):
        # 如果发现 fast 指向的元素与 slow 指向的不同
        # 说明找到了一个新的唯一元素
        if nums[fast] != nums[slow]:
            # 慢指针前移一位
            slow += 1
            # 将新元素覆盖到慢指针位置
            nums[slow] = nums[fast]
            
    # 返回长度，即 slow 索引 + 1
    return slow + 1

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
