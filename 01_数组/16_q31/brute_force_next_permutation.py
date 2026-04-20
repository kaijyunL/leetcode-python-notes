import itertools
from typing import List

def brute_force_next_permutation(nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    
    解法一：暴力法 (Brute Force)
    思路：生成全排列，排序，找出下一个。
    注意：在 LeetCode 提交此代码对于大数组会超时。
    """
    # 1. 复制原数组
    n = len(nums)
    if n <= 1:
        return
        
    # 2. 获取原数组的元组表示（用于比较）
    current_nums = tuple(nums)
    
    # 3. 将现有的数字排序，生成所有排列
    # itertools.permutations 会按输入元素的顺序生成。为了确得字典序，我们先排序。
    all_sorted_elements = sorted(nums)
    all_perms = sorted(list(set(itertools.permutations(all_sorted_elements))))
    
    # 4. 找到当前序列在所有全排列中的位置
    try:
        idx = all_perms.index(current_nums)
        # 5. 取下一个序列。如果是最后一个，取第一个。
        next_idx = (idx + 1) % len(all_perms)
        next_perm = all_perms[next_idx]
        
        # 6. 原地修改数组
        for i in range(n):
            nums[i] = next_perm[i]
    except ValueError:
        # 如果数组中原本就不存在（实际不应该发生），执行升序排列
        nums.sort()

# 测试用例
if __name__ == "__main__":
    example1 = [1, 2, 3]
    brute_force_next_permutation(example1)
    print(f"输入: [1, 2, 3] -> 输出: {example1}") # 期望: [1, 3, 2]

    example2 = [3, 2, 1]
    brute_force_next_permutation(example2)
    print(f"输入: [3, 2, 1] -> 输出: {example2}") # 期望: [1, 2, 3]

    example3 = [1, 1, 5]
    brute_force_next_permutation(example3)
    print(f"输入: [1, 1, 5] -> 输出: {example3}") # 期望: [1, 5, 1]
