# LeetCode 27: 移除元素 - 暴力解法
# 时间复杂度: O(n^2)
# 空间复杂度: O(1)

def remove_element_brute_force(nums, val):
    """
    使用嵌套循环，发现目标值后将后续所有元素前移
    """
    size = len(nums)
    i = 0
    while i < size:
        if nums[i] == val:
            # 发现目标值，将后面的元素全部向前挪一位
            for j in range(i + 1, size):
                nums[j - 1] = nums[j]
            size -= 1  # 数组长度减一
            # 重要：下面不需要 i += 1，因为当前 i 位置已经是新挪过来的元素，需要重检
            continue 
        i += 1
    return size

if __name__ == "__main__":
    # 测试用例
    test_nums = [0, 1, 2, 2, 3, 0, 4, 2]
    test_val = 2
    print(f"原数组: {test_nums}, 移除值: {test_val}")
    
    new_len = remove_element_brute_force(test_nums, test_val)
    
    print(f"新长度: {new_len}")
    print(f"修改后的数组前部: {test_nums[:new_len]}")
    
    # 验证答案
    assert new_len == 5
    assert sorted(test_nums[:new_len]) == sorted([0, 1, 3, 0, 4])
    print("测试通过！")
