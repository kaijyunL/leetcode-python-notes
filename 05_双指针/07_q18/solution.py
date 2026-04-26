class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        """
        使用双指针法解决四数之和问题。
        时间复杂度: O(N^3)
        空间复杂度: O(log N) (取决于排序算法)
        """
        res = []
        n = len(nums)
        if n < 4:
            return res
        
        nums.sort()
        
        for i in range(n - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
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
                
                left, right = j + 1, n - 1
                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]
                    
                    if total == target:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        
                        left += 1
                        right -= 1
                        
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
                    elif total < target:
                        left += 1
                    else:
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
        
        nums.sort()
        res = []

        for i in range(n - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
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
                
                remaining_target = target - nums[i] - nums[j]
                two_sum_pairs = self.twoSum(nums, remaining_target, j + 1)
                
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
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
            elif s < target:
                left += 1
            else:
                right -= 1
        return res

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
