from typing import List

def twoSum(numbers: List[int], target: int) -> List[int]:
    n = len(numbers)
    for i in range(n):
        for j in range(i + 1, n):
            if numbers[i] + numbers[j] == target:
                return [i + 1, j + 1]
    return []

if __name__ == "__main__":
    # 测试样例
    nums = [2, 7, 11, 15]
    target = 9
    print(f"输入: numbers = {nums}, target = {target}")
    print(f"输出: {twoSum(nums, target)}")
