def longest_consecutive(nums):
    """
    暴力解法：对于每个数字，不断检查其后继数字是否存在于列表中。
    时间复杂度：O(n^3) - 外层循环 n，while 循环最多 n，列表查找 'in' 操作是 O(n)。
    """
    longest_streak = 0

    for num in nums:
        current_num = num
        current_streak = 1

        # 在列表中查找 current_num + 1
        # 注意：Python 的 `x in list` 操作的时间复杂度是 O(n)
        while current_num + 1 in nums:
            current_num += 1
            current_streak += 1

        longest_streak = max(longest_streak, current_streak)

    return longest_streak

if __name__ == "__main__":
    # 测试用例
    test_nums = [100, 4, 200, 1, 3, 2]
    print(f"--- 暴力解法 ---")
    print(f"输入: {test_nums}")
    result = longest_consecutive(test_nums)
    print(f"结果: {result}")
    assert result == 4
