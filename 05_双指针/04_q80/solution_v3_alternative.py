from typing import List

def removeDuplicates(nums: List[int]):
    # 方法 3：基于用户提供的 [slow=0, fast=1] 起始逻辑续写
    if len(nums) < 3:
        return len(nums)

    slow, fast = 0, 1
    count = 1
    
    while fast < len(nums):
        if nums[fast] == nums[slow]:
            if count < 2:
                count += 1
                slow += 1
                nums[slow] = nums[fast]
            # 如果 count >= 2，说明已经有两个了，fast 继续走，slow 不动
        else:
            # 遇到了新数字，重置计数器
            count = 1
            slow += 1
            nums[slow] = nums[fast]
        
        fast += 1
        
    return slow + 1

# 测试代码
if __name__ == "__main__":
    test_nums = [1, 1, 1, 2, 2, 3]
    length = removeDuplicates(test_nums)
    print(f"新长度: {length}, 数组内容: {test_nums[:length]}")
