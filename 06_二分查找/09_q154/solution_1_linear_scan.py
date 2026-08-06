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

    assert solution.findMin([1, 3, 5]) == 1
    assert solution.findMin([2, 2, 2, 0, 1]) == 0
    assert solution.findMin([2, 2, 2, 0, 1, 2]) == 0
    assert solution.findMin([10, 1, 10, 10, 10]) == 1
    assert solution.findMin([1, 1, 1, 1]) == 1
    assert solution.findMin([1]) == 1
    assert solution.findMin([3, 3, 1, 3]) == 1

    print("all tests passed")
