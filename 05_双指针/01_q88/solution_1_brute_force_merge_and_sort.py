# 方法1：暴力合并后排序


class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        暴力：把 nums2 塞进 nums1 后半段，再排序。
        时间复杂度: O((m+n)log(m+n))
        空间复杂度: O(log(m+n))
        """
        nums1[m:] = nums2
        nums1.sort()


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
