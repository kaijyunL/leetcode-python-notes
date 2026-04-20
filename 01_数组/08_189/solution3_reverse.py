from typing import List

def rotate(nums: List[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    n = len(nums)
    k %= n
    
    # 辅助函数：反转数组指定范围 [left, right] 的元素
    def reverse(left: int, right: int) -> None:
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
            
    # 1. 翻转整个数组
    reverse(0, n - 1)
    # 2. 翻转前 k 个元素
    reverse(0, k - 1)
    # 3. 翻转剩余元素
    reverse(k, n - 1)

# 测试代码
if __name__ == "__main__":
    test_nums = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    print(f"原数组: {test_nums}, k = {k}")
    rotate(test_nums, k)
    print(f"轮转后: {test_nums}")
