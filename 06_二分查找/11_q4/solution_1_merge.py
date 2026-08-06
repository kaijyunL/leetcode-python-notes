# 方法1：双指针合并


class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        merged = []
        i = 0
        j = 0

        while i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                merged.append(nums1[i])
                i += 1
            else:
                merged.append(nums2[j])
                j += 1

        merged.extend(nums1[i:])
        merged.extend(nums2[j:])

        total_len = len(merged)
        mid = total_len // 2

        if total_len % 2 == 1:
            return float(merged[mid])

        return (merged[mid - 1] + merged[mid]) / 2


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

    print("all tests passed")
