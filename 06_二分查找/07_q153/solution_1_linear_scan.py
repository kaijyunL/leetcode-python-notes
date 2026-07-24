# 方法1：线性扫描


class Solution:
    def findMin(self, nums: list[int]) -> int:
        ans = nums[0]

        for num in nums:
            if num < ans:
                ans = num

        return ans


if __name__ == "__main__":
    solution = Solution()

    assert solution.findMin([3, 4, 5, 1, 2]) == 1
    assert solution.findMin([4, 5, 6, 7, 0, 1, 2]) == 0
    assert solution.findMin([11, 13, 15, 17]) == 11
    assert solution.findMin([1]) == 1
    assert solution.findMin([2, 1]) == 1
    assert solution.findMin([5, 1, 2, 3, 4]) == 1

    print("all tests passed")
