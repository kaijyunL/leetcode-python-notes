from typing import List

def twoSum(numbers: List[int], target: int) -> List[int]:
    left = 0
    right = len(numbers) - 1
    
    while left < right:
        current_sum = numbers[left] + numbers[right]
        if current_sum == target:
            return [left + 1, right + 1]
        elif current_sum < target:
            # 和太小，左指针右移以增大和
            left += 1
        else:
            # 和太大，右指针左移以减小和
            right -= 1
    return []

if __name__ == "__main__":
    # 测试样例
    nums = [-1, 0]
    target = -1
    print(f"输入: numbers = {nums}, target = {target}")
    print(f"输出: {twoSum(nums, target)}")
