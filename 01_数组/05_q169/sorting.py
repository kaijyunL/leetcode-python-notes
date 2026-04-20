from typing import List

def majority_element_sorting(nums: List[int]) -> int:
    """
    排序法：中位数即为多数元素。
    时间复杂度: O(n log n)
    空间复杂度: O(1) 或 O(n) (Python 的 sort 取决于实现)
    """
    # 将数组原地排序
    nums.sort()
    
    # 只要返回数组中间位置的数即可
    return nums[len(nums) // 2]

# 测试代码
if __name__ == "__main__":
    test_nums = [2, 2, 1, 1, 1, 2, 2]
    print(f"输入: {test_nums}")
    print(f"多数元素 (排序法): {majority_element_sorting(test_nums)}")
