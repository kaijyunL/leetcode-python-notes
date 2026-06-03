def longest_consecutive(nums):
    """
    哈希集合最优解：利用 set 的 O(1) 查找特性，并只从序列起点开始枚举。
    时间复杂度：O(n) - 每个数字最多被访问两次。
    空间复杂度：O(n) - 需要一个集合存储所有数字。
    """
    longest_streak = 0
    # 将列表转换为集合，去重且查找复杂度降为 O(1)
    num_set = set(nums)

    for num in num_set:
        # 核心逻辑：如果 num-1 不在集合中，说明 num 是该连续序列的“起点”
        # 这个简单的判断保证了内层 while 循环总共只会执行 n 次
        if num - 1 not in num_set:
            current_num = num
            current_streak = 1

            # 不断查找后继数字
            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1

            # 更新全局最大长度
            longest_streak = max(longest_streak, current_streak)

    return longest_streak

if __name__ == "__main__":
    # 测试用例
    test_nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
    print(f"--- 哈希集合最优解 ---")
    print(f"输入: {test_nums}")
    result = longest_consecutive(test_nums)
    print(f"结果: {result}")
    # 0, 1, 2, 3, 4, 5, 6, 7, 8 长度为 9
    assert result == 9
