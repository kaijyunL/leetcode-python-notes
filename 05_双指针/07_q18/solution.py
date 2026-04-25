import math

class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        """
        使用双指针法解决四数之和问题。
        时间复杂度: O(N^3)
        空间复杂度: O(log N) (取决于排序算法)
        """
        res = []
        n = len(nums)
        # 基础判断：如果数字少于4个，直接返回空
        if n < 4:
            return res
        
        # 1. 排序是双指针的前提
        nums.sort()
        
        # 2. 第一层循环：固定第一个数 nums[i]
        for i in range(n - 3):
            # 去重：如果当前值和上一个值相同，跳过（第一个数除外）
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            # --- 剪枝优化1 ---
            # 如果当前最小的四个数之和已经大于 target，后面更大的数更不可能满足，直接结束
            if nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3] > target:
                break
            
            # --- 剪枝优化2 ---
            # 如果当前数加上最大的三个数之和仍小于 target，说明当前 i 太小，跳过找下一个更大的 i
            if nums[i] + nums[n - 3] + nums[n - 2] + nums[n - 1] < target:
                continue

            # 3. 第二层循环：固定第二个数 nums[j]
            for j in range(i + 1, n - 2):
                # 去重：如果当前值和上一个值相同，跳过（第二个数从 i+1 开始算起）
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                
                # --- 针对 j 的剪枝优化 ---
                if nums[i] + nums[j] + nums[j + 1] + nums[j + 2] > target:
                    break
                if nums[i] + nums[j] + nums[n - 2] + nums[n - 1] < target:
                    continue
                
                # 4. 双指针寻找剩余的两个数
                left, right = j + 1, n - 1
                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]
                    
                    if total == target:
                        # 找到一组解
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        
                        # 重要：跳过重复的 left 和 right 值，避免结果集重复
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        
                        # 移动指针寻找下一组可能
                        left += 1
                        right -= 1
                    elif total < target:
                        # 和太小，左指针右移以增大和
                        left += 1
                    else:
                        # 和太大，右指针左移以减小和
                        right -= 1
        
        return res

    def fourSumWithTwoSum(self, nums: list[int], target: int) -> list[list[int]]:
        """
        方式二：通过抽象出的 twoSum 函数来解决四数之和。
        这种方式结构更清晰，展示了如何从 n-sum 降维到 2-sum，逻辑更易维护。
        """
        n = len(nums)
        if n < 4:
            return []
        
        # 为了演示两套方案，这里假设输入已经排过序，或者在函数内部再排一次（不影响正确性）
        nums.sort()
        res = []

        for i in range(n - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            # 使用与 fourSum 相同的剪枝策略
            if nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3] > target:
                break
            if nums[i] + nums[n - 3] + nums[n - 2] + nums[n - 1] < target:
                continue

            for j in range(i + 1, n - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                
                if nums[i] + nums[j] + nums[j + 1] + nums[j + 2] > target:
                    break
                if nums[i] + nums[j] + nums[n - 2] + nums[n - 1] < target:
                    continue
                
                # --- 核心抽象：调用独立的两数之和函数 ---
                remaining_target = target - numsrew[i] - nums[j]
                two_sum_pairs = self.twoSum(nums, remaining_target, j + 1)
                
                # 将两数之和的结果与前导的 i, j 组合
                for pair in two_sum_pairs:
                    res.append([nums[i], nums[j]] + pair)
        
        return res

    def twoSum(self, nums: list[int], target: int, start: int) -> list[list[int]]:
        """
        抽象的双指针两数之和实现（用于有序数组）。
        """
        res = []
        left, right = start, len(nums) - 1
        
        while left < right:
            s = nums[left] + nums[right]
            if s == target:
                res.append([nums[left], nums[right]])
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1
            elif s < target:
                left += 1
            else:
                right -= 1
        return res

# --- 测试代码 ---
if __name__ == "__main__":
    sol = Solution()
    
    test_cases = [
        ([1, 0, -1, 0, -2, 2], 0),
        ([2, 2, 2, 2, 2], 8)
    ]

    for nums, target in test_cases:
        print(f"\n输入: nums = {nums}, target = {target}")
        print(f"方法1 (fourSum) 输出: {sol.fourSum(nums, target)}")
        print(f"方法2 (fourSumWithTwoSum) 输出: {sol.fourSumWithTwoSum(nums, target)}")
if __name__ == "__main__":
    sol = Solution()
    
    # 示例 1
    nums1 = [1, 0, -1, 0, -2, 2]
    target1 = 0
    print(f"输入: nums = {nums1}, target = {target1}")
    print(f"输出: {sol.fourSum(nums1, target1)}")
    # 预期输出: [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]

    # 示例 2
    nums2 = [2, 2, 2, 2, 2]
    target2 = 8
    print(f"\n输入: nums = {nums2}, target = {target2}")
    print(f"输出: {sol.fourSum(nums2, target2)}")
    # 预期输出: [[2, 2, 2, 2]]
