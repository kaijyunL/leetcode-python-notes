# 方法2：正向双指针 + 辅助数组


class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        正向双指针：两个指针从前往后比，小的先进辅助数组。
        时间复杂度: O(m+n)
        空间复杂度: O(m+n)
        """
        sorted_arr = []
        p1, p2 = 0, 0

        while p1 < m and p2 < n:
            if nums1[p1] <= nums2[p2]:
                sorted_arr.append(nums1[p1])
                p1 += 1
            else:
                sorted_arr.append(nums2[p2])
                p2 += 1

        if p1 < m:
            sorted_arr.extend(nums1[p1:m])
        if p2 < n:
            sorted_arr.extend(nums2[p2:n])

        nums1[:] = sorted_arr


def run_test() -> None:
    solver = Solution()

    nums1 = [1, 2, 3, 0, 0, 0]
    solver.merge(nums1, 3, [2, 5, 6], 3)
    assert nums1 == [1, 2, 2, 3, 5, 6]

    nums1 = [1]
    solver.merge(nums1, 1, [], 0)
    assert nums1 == [1]

    nums1 = [0]
    solver.merge(nums1, 0, [1], 1)
    assert nums1 == [1]

    nums1 = [4, 5, 6, 0, 0, 0]
    solver.merge(nums1, 3, [1, 2, 3], 3)
    assert nums1 == [1, 2, 3, 4, 5, 6]

    nums1 = [1, 2, 4, 5, 6, 0]
    solver.merge(nums1, 5, [3], 1)
    assert nums1 == [1, 2, 3, 4, 5, 6]


if __name__ == "__main__":
    run_test()
    print("all tests passed")
