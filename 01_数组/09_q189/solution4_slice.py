from typing import List

def rotate(nums: List[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    n = len(nums)
    k %= n
    
    # 必须要用 nums[:] = ... 来保证原地修改
    # 否则只是改变了局部变量 nums 的指向，外部数组不会变
    nums[:] = nums[n-k:] + nums[:n-k]

# 测试代码
if __name__ == "__main__":
    test_nums = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    print(f"原数组: {test_nums}, k = {k}")
    rotate(test_nums, k)
    print(f"轮转后: {test_nums}")
