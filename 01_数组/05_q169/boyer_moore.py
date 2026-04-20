from typing import List

def majority_element_boyer_moore(nums: List[int]) -> int:
    """
    摩尔投票法 (最优解)：两两抵消。
    时间复杂度: O(n)
    空间复杂度: O(1)
    """
    count = 0
    candidate = None

    for num in nums:
        # 当计数为 0 时，任命当前数字为新的候选人
        if count == 0:
            candidate = num
        
        if num == candidate:
            count += 1
        else:
            count -= 1

    return candidate

# 测试代码
if __name__ == "__main__":
    test_nums = [2, 2, 1, 1, 1, 2, 2]
    # 执行流程演示:
    # 2 -> count=1, cand=2
    # 2 -> count=2, cand=2
    # 1 -> count=1, cand=2
    # 1 -> count=0, cand=2
    # 1 -> count=1, cand=1
    # 2 -> count=0, cand=1
    # 2 -> count=1, cand=2
    # 最终结果: 2
    print(f"输入: {test_nums}")
    print(f"多数元素 (摩尔投票法): {majority_element_boyer_moore(test_nums)}")
