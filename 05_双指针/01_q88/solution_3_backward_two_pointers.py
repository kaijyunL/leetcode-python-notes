# 方法3：逆向双指针（面试主推）


class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        逆向双指针：从后往前比，大数填后面，利用 nums1 末尾空闲位。
        时间复杂度: O(m+n)
        空间复杂度: O(1)
        """
        p1, p2 = m - 1, n - 1
        p = m + n - 1

        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1

        while p2 >= 0:
            nums1[p] = nums2[p2]
            p -= 1
            p2 -= 1


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
