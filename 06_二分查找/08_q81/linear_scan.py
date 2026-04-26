class Solution:
    def search(self, nums: list[int], target: int) -> bool:
        """
        线性扫描：逐个查找 target
        时间复杂度: O(n)
        空间复杂度: O(1)
        """
        for num in nums:
            if num == target:
                return True

        return False


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        ([2, 5, 6, 0, 0, 1, 2], 0),
        ([2, 5, 6, 0, 0, 1, 2], 3),
        ([1, 0, 1, 1, 1], 0),
        ([1, 1, 1, 1, 1], 2),
        ([1], 1),
        ([1, 3, 1, 1, 1], 3),
    ]

    for nums, target in test_cases:
        print(f"nums = {nums}, target = {target}, result = {solution.search(nums, target)}")
