# LeetCode 27: 移除元素 - 快慢指针解法
# 时间复杂度: O(n)
# 空间复杂度: O(1)

def remove_element_two_pointers(nums, val):
    """
    快慢指针：
    快指针负责遍历数组寻找符合条件的元素
    慢指针负责指向新数组存储的位置
    """
    slow = 0
    for fast in range(len(nums)):
        if nums[fast] != val:
            nums[slow] = nums[fast]
            slow += 1
    return slow

if __name__ == "__main__":
    # 测试用例
    test_nums = [0, 1, 2, 2, 3, 0, 4, 2]
    test_val = 2
    print(f"原数组: {test_nums}, 移除值: {test_val}")
    
    new_len = remove_element_two_pointers(test_nums, test_val)
    
    print(f"新长度: {new_len}")
    print(f"修改后的数组前部: {test_nums[:new_len]}")
    
    # 验证答案
    assert new_len == 5
    assert sorted(test_nums[:new_len]) == sorted([0, 1, 3, 0, 4])
    print("测试通过！")
