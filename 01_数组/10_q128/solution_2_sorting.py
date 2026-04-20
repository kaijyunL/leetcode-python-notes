def longest_consecutive(nums):
    """
    排序解法：先排序，使连续数字排列在一起。
    时间复杂度：O(n log n) - 排序的时间
    """
    if not nums:
        return 0

    # 原地排序
    nums.sort()

    longest_streak = 1
    current_streak = 1

    for i in range(1, len(nums)):
        # 如果当前数字和前一个数字不相等，才进行逻辑处理
        if nums[i] != nums[i - 1]:
            # 判断是否连续
            if nums[i] == nums[i - 1] + 1:
                current_streak += 1
            else:
                # 序列断开，更新最大长度并重置计数器
                longest_streak = max(longest_streak, current_streak)
                current_streak = 1
    
    # 最后还要比较一次，防止最后一个序列是最长的
    return max(longest_streak, current_streak)

if __name__ == "__main__":
    # 测试用例
    test_nums = [100, 4, 200, 1, 3, 2]
    print(f"--- 排序解法 ---")
    print(f"输入: {test_nums}")
    result = longest_consecutive(test_nums)
    print(f"结果: {result}")
    assert result == 4

    test_nums_2 = [0, 1, 1, 2]
    print(f"输入 (含重复): {test_nums_2}")
    result_2 = longest_consecutive(test_nums_2)
    print(f"结果: {result_2}")
    assert result_2 == 3
