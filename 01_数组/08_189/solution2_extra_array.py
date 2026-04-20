from typing import List

def rotate(nums: List[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    n = len(nums)
    k %= n
    
    # 1. 创建一个同样大小的数组
    temp = [0] * n
    
    # 2. 计算每个元素的新位置
    for i in range(n):
        temp[(i + k) % n] = nums[i]
        
    # 3. 将结果复制回原数组
    for i in range(n):
        nums[i] = temp[i]

# 测试代码
if __name__ == "__main__":
    test_nums = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    print(f"原数组: {test_nums}, k = {k}")
    rotate(test_nums, k)
    print(f"轮转后: {test_nums}")
