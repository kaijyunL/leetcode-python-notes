# LeetCode 27: 移除元素 - 左右指针进阶优化 (减少赋值操作)
# 时间复杂度: O(n)
# 空间复杂度: O(1)

def remove_element_optimized(nums, val):
    """
    左右指针：
    当左指针发现目标值时，直接将数组末尾的元素搬过来覆盖。
    这种方法在需要移除的元素很少时，赋值操作最少。
    """
    left = 0
    right = len(nums)
    while left < right:
        if nums[left] == val:
            # 发现目标，将末尾元素移到这里
            nums[left] = nums[right - 1]
            # 缩减检查范围
            right -= 1
            # 注意：left 这次不增加，因为刚换过来的末尾元素还没检查
        else:
            left += 1
    return left

if __name__ == "__main__":
    # 测试用例
    test_nums = [0, 1, 2, 2, 3, 0, 4, 2]
    test_val = 2
    print(f"原数组: {test_nums}, 移除值: {test_val}")
    
    new_len = remove_element_optimized(test_nums, test_val)
    
    print(f"新长度: {new_len}")
    print(f"修改后的数组前部: {test_nums[:new_len]}")
    
    # 验证答案
    assert new_len == 5
    assert sorted(test_nums[:new_len]) == sorted([0, 1, 3, 0, 4])
    print("测试通过！")
