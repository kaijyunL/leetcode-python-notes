class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        """
        暴力破解方法 (Brute Force)
        时间复杂度: O(n^3) - 三层嵌套循环
        空间复杂度: O(1) - 除了结果之外没有使用额外的数据结构
        """
        n = len(nums)
        # 初始最接近的和设为无限大或前三个数的和
        # 我们用 res 来保存当前发现的最接近 target 的和
        res = sum(nums[:3])
        
        # 三重循环遍历所有可能的三元组
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    # 当前三元组的和
                    current_sum = nums[i] + nums[j] + nums[k]
                    
                    # 比较当前和与 res，看谁更接近 target
                    # abs(current_sum - target) < abs(res - target) 时更新
                    if abs(current_sum - target) < abs(res - target):
                        res = current_sum
        
        # 返回找到的那个最接近 target 的和
        return res

# 测试代码
if __name__ == "__main__":
    s = Solution()
    print(s.threeSumClosest([-1, 2, 1, -4], 1))  # 期望输出: 2 (因为 -1 + 2 + 1 = 2)
