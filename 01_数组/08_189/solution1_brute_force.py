from typing import List

def rotate(nums: List[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    n = len(nums)
    k %= n # 处理 k 大于数组长度的情况
    
    # 向右轮转 k 次
    for _ in range(k):
        # 1. 保存最后一个元素
        previous = nums[-1]
        # 2. 将数组元素依次向右移动一位
        for i in range(n):
            nums[i], previous = previous, nums[i]
            
    # 另一种更直观的写法：
    # for _ in range(k):
    #     last = nums[n - 1]
    #     for j in range(n - 1, 0, -1):
    #         nums[j] = nums[j - 1]
    #     nums[0] = last

# 测试代码
if __name__ == "__main__":
    test_nums = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    print(f"原数组: {test_nums}, k = {k}")
    rotate(test_nums, k)
    print(f"轮转后: {test_nums}")
