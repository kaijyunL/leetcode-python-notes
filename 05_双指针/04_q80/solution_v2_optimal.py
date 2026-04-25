from typing import List

def removeDuplicates(nums: List[int]) -> int:
    """
    最优解法：双指针法
    利用数组有序的特点，通过 fast 指针遍历，slow 指针记录新位置。
    """
    n = len(nums)
    if n <= 2:
        return n
    
    # slow 指针表示下一个待插入的位置
    # 因为前两个元素必然符合要求，所以从下标 2 开始
    slow = 2
    
    for fast in range(2, n):
        # 核心逻辑：检查当前 fast 指向的元素是否与 slow 位置向前数两个的元素相同
        # 如果不同，说明 nums[fast] 放到 nums[slow] 位置后，不会连续出现超过 2 次
        if nums[fast] != nums[slow - 2]:
            nums[slow] = nums[fast]
            slow += 1
            
    return slow

# 测试代码
if __name__ == "__main__":
    test_nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]
    length = removeDuplicates(test_nums)
    print(f"新长度: {length}, 数组内容: {test_nums[:length]}")
