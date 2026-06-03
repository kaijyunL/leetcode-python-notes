from typing import List
from collections import Counter

def majority_element_hash_map(nums: List[int]) -> int:
    """
    哈希表法：利用计数器记录每个数出现的次数。
    时间复杂度: O(n)
    空间复杂度: O(n)
    """
    # 使用 Python 内置的 Counter 方便计数
    counts = Counter(nums)
    
    # 只要返回出现次数最多的键即可，
    # 或者手动遍历以符合题目 "大于 n/2" 的定义
    return max(counts.keys(), key=counts.get)

def majority_element_hash_map_manual(nums: List[int]) -> int:
    """
    手动实现哈希表计数。
    """
    counts = {}
    threshold = len(nums) // 2
    for num in nums:
        counts[num] = counts.get(num, 0) + 1
        if counts[num] > threshold:
            return num

# 测试代码
if __name__ == "__main__":
    test_nums = [2, 2, 1, 1, 1, 2, 2]
    print(f"输入: {test_nums}")
    print(f"多数元素 (哈希表法): {majority_element_hash_map(test_nums)}")
    print(f"多数元素 (哈希表手动实现): {majority_element_hash_map_manual(test_nums)}")
