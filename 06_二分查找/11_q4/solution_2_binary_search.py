# 方法2：二分查找分割点（面试主推）


class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m = len(nums1)
        n = len(nums2)
        total_left = (m + n + 1) // 2

        left = 0
        right = m

        while left <= right:
            i = (left + right) // 2
            j = total_left - i

            nums1_left = float("-inf") if i == 0 else nums1[i - 1]
            nums1_right = float("inf") if i == m else nums1[i]
            nums2_left = float("-inf") if j == 0 else nums2[j - 1]
            nums2_right = float("inf") if j == n else nums2[j]

            if nums1_left <= nums2_right and nums2_left <= nums1_right:
                if (m + n) % 2 == 1:
                    return float(max(nums1_left, nums2_left))

                left_max = max(nums1_left, nums2_left)
                right_min = min(nums1_right, nums2_right)
                return (left_max + right_min) / 2

            if nums1_left > nums2_right:
                right = i - 1
            else:
                left = i + 1

        raise ValueError("input arrays are invalid")


if __name__ == "__main__":
    solution = Solution()

    assert solution.findMedianSortedArrays([1, 3], [2]) == 2.0
    assert solution.findMedianSortedArrays([1, 2], [3, 4]) == 2.5
    assert solution.findMedianSortedArrays([], [1]) == 1.0
    assert solution.findMedianSortedArrays([2], []) == 2.0
    assert solution.findMedianSortedArrays([0, 0], [0, 0]) == 0.0
    assert solution.findMedianSortedArrays([1, 3, 8], [7, 9, 10, 11]) == 8.0
    assert solution.findMedianSortedArrays([-5, -3, -1], [-2]) == -2.5
    assert solution.findMedianSortedArrays([1, 1], [1, 2]) == 1.0
    assert solution.findMedianSortedArrays([100000], [100001]) == 100000.5

    print("all tests passed")
