class Solution:
    def search(self, nums: list[int], target: int) -> int:
        """
        线性扫描：逐个查找 target
        时间复杂度: O(n)
        空间复杂度: O(1)
        """
        for index, num in enumerate(nums):
            if num == target:
                return index

        return -1


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        ([4, 5, 6, 7, 0, 1, 2], 0),
        ([4, 5, 6, 7, 0, 1, 2], 3),
        ([1], 0),
        ([1], 1),
        ([3, 1], 1),
    ]

    for nums, target in test_cases:
        print(f"nums = {nums}, target = {target}, result = {solution.search(nums, target)}")
