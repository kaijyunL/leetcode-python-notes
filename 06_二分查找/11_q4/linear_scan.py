class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        """
        线性合并：合并两个有序数组后取中位数
        时间复杂度: O(m + n)
        空间复杂度: O(m + n)
        """
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

        n = len(merged)
        mid = n // 2

        if n % 2 == 1:
            return float(merged[mid])

        return (merged[mid - 1] + merged[mid]) / 2


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        ([1, 3], [2]),
        ([1, 2], [3, 4]),
        ([], [1]),
        ([2], []),
        ([0, 0], [0, 0]),
        ([1, 3, 8], [7, 9, 10, 11]),
    ]

    for nums1, nums2 in test_cases:
        result = solution.findMedianSortedArrays(nums1, nums2)
        print(f"nums1 = {nums1}, nums2 = {nums2}, result = {result}")
