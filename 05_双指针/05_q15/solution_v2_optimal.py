from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        最优解法：排序 + 双指针
        时间复杂度: O(N^2)
        空间复杂度: O(1) (除结果列表外)
        """
        n = len(nums)
        nums.sort()
        res = []
        
        for i in range(n):
            # 如果当前数大于0，后面两个数也一定大于0，和不可能为0
            if nums[i] > 0:
                break
            
            # 外层去重：跳过相同的数字
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            # 双指针寻找另外两个数
            left = i + 1
            right = n - 1
            
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                
                if total == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    # 内层去重：跳过左边重复数字
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    # 内层去重：跳过右边重复数字
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1
                    
        return res

if __name__ == "__main__":
    s = Solution()
    test_nums = [-1, 0, 1, 2, -1, -4]
    print(f"输入: {test_nums}")
    print(f"输出: {s.threeSum(test_nums)}")
