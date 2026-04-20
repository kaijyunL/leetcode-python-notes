from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # 第一步：将 nums2 复制到 nums1 的后半部分
        nums1[m:] = nums2
        
        # 第二步：对整个 nums1 进行排序
        nums1.sort()

if __name__ == "__main__":
    # 测试用例
    n1 = [1, 2, 3, 0, 0, 0]
    m_val = 3
    n2 = [2, 5, 6]
    n_val = 3
    Solution().merge(n1, m_val, n2, n_val)
    print(f"暴力合并后排序结果: {n1}")
