from typing import List

def removeDuplicates(nums: List[int]) -> int:
    """
    暴力解法：遍历数组，统计每个数字出现的次数。
    如果发现某个数字出现超过 2 次，则利用 pop 删除多余元素。
    """
    if not nums:
        return 0
    
    i = 0
    count = 1
    while i < len(nums) - 1:
        if nums[i] == nums[i + 1]:
            count += 1
            if count > 2:
                # 出现超过2次，删除当前位置的下一个元素
                nums.pop(i + 1)
                # 注意：pop 之后不需要增加 i，因为下一位补上来了
            else:
                i += 1
        else:
            # 遇到新数字，计数器重置
            count = 1
            i += 1
            
    return len(nums)

# 测试代码
if __name__ == "__main__":
    test_nums = [1, 1, 1, 2, 2, 3]
    length = removeDuplicates(test_nums)
    print(f"新长度: {length}, 数组内容: {test_nums[:length]}")
