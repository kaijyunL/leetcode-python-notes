from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        暴力解法：三层循环 + 集合去重
        时间复杂度: O(N^3)
        空间复杂度: O(N)
        """
        n = len(nums)
        res = set()
        # 先排序是为了方便最后三元组放入集合时统一顺序，从而去重
        nums.sort()
        
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if nums[i] + nums[j] + nums[k] == 0:
                        # 排序后的三元组放入 set 会自动去重
                        res.add((nums[i], nums[j], nums[k]))
                        
        return [list(triplet) for triplet in res]

if __name__ == "__main__":
    s = Solution()
    test_nums = [-1, 0, 1, 2, -1, -4]
    print(f"输入: {test_nums}")
    print(f"输出: {s.threeSum(test_nums)}")
