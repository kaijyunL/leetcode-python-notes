class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        """
        优化方法: 排序 + 双指针 (Sorting + Two Pointers)
        时间复杂度: O(n^2)
        空间复杂度: O(log n) 或 O(1) 取决于排序算法的实现
        """
        # 第一步：排序，这一步非常重要，是后续双指针的基础
        nums.sort()
        n = len(nums)
        # 初始结果设为前三个数的和
        res = nums[0] + nums[1] + nums[2]
        
        # 第二步：固定第一个数 nums[i]，寻找剩下两个数
        for i in range(n - 2):
            # 优化：如果 i 和之前的 i-1 重复，可以跳过（虽然不跳过也行，但跳过效率更高）
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            # 使用双指针 left 和 right
            left, right = i + 1, n - 1
            
            while left < right:
                # 当前三元组的和
                current_sum = nums[i] + nums[left] + nums[right]
                
                # 如果这个和正好等于 target，说明我们找到了最接近的解
                if current_sum == target:
                    return target
                
                # 比较当前和与 res，哪个更接近 target 就更新 res
                if abs(current_sum - target) < abs(res - target):
                    res = current_sum
                
                # 双指针移动逻辑:
                # 如果 current_sum < target，我们需要更大的和，左指针向右移
                if current_sum < target:
                    left += 1
                    # 跳过重复的 left (可选，提高性能)
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                # 如果 current_sum > target，我们需要更小的和，右指针向左移
                else:
                    right -= 1
                    # 跳过重复的 right (可选，提高性能)
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
        
        return res

# 测试代码
if __name__ == "__main__":
    solution = Solution()
    print(solution.threeSumClosest([-1, 2, 1, -4], 1))  # 输出: 2 (-1 + 2 + 1)
    print(solution.threeSumClosest([0, 0, 0], 1))       # 输出: 0 (0 + 0 + 0)
