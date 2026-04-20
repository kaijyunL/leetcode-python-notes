from typing import List

def twoSum(numbers: List[int], target: int) -> List[int]:
    n = len(numbers)
    for i in range(n):
        low = i + 1
        high = n - 1
        complement = target - numbers[i]
        
        # 在右侧部分进行二分查找
        while low <= high:
            mid = (low + high) // 2
            if numbers[mid] == complement:
                return [i + 1, mid + 1]
            elif numbers[mid] < complement:
                low = mid + 1
            else:
                high = mid - 1
    return []

if __name__ == "__main__":
    # 测试样例
    nums = [2, 3, 4]
    target = 6
    print(f"输入: numbers = {nums}, target = {target}")
    print(f"输出: {twoSum(nums, target)}")
