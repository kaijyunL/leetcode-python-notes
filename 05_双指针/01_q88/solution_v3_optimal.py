from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        最优解：逆向双指针
        从后往前填补 nums1，利用 nums1 末尾的空闲空间，达到 O(1) 空间复杂度。
        """
        # p1 指向 nums1 有效元素的末尾
        # p2 指向 nums2 的末尾
        # p 指向 nums1 最终合并位置的末尾
        p1, p2, p = m - 1, n - 1, m + n - 1
        
        # 从后往前比较并填充
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1
            
        # 如果 nums2 还有剩余，将其复制到 nums1 前面
        # (如果 nums1 还有剩余则不需要动，因为它们已经在正确的位置上了)
        while p2 >= 0:
            nums1[p] = nums2[p2]
            p -= 1
            p2 -= 1

if __name__ == "__main__":
    n1 = [1, 2, 3, 0, 0, 0]
    m_val = 3
    n2 = [2, 5, 6]
    n_val = 3
    Solution().merge(n1, m_val, n2, n_val)
    print(f"最优解 (逆向双指针) 结果: {n1}")
