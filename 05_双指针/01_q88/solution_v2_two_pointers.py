from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        使用辅助数组的正向双指针解法
        """
        # 创建辅助数组保存结果
        sorted_array = []
        p1, p2 = 0, 0
        
        # 依次比较两个数组的元素
        while p1 < m and p2 < n:
            if nums1[p1] <= nums2[p2]:
                sorted_array.append(nums1[p1])
                p1 += 1
            else:
                sorted_array.append(nums2[p2])
                p2 += 1
        
        # 处理剩余元素
        if p1 < m:
            sorted_array.extend(nums1[p1:m])
        if p2 < n:
            sorted_array.extend(nums2[p2:n])
            
        # 将结果写回 nums1
        nums1[:] = sorted_array

if __name__ == "__main__":
    n1 = [1, 2, 3, 0, 0, 0]
    m_val = 3
    n2 = [2, 5, 6]
    n_val = 3
    Solution().merge(n1, m_val, n2, n_val)
    print(f"正向双指针结果: {n1}")
