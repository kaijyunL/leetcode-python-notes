from functools import cmp_to_key


class Solution:
    def largestNumber(self, nums: list[int]) -> str:
        """
        解法2：自定义排序比较 — 面试推荐
        时间复杂度: O(n log n)
        空间复杂度: O(n)
        """
        strs = [str(x) for x in nums]

        def cmp(a: str, b: str) -> int:
            if a + b > b + a:
                return -1
            elif a + b < b + a:
                return 1
            else:
                return 0

        strs.sort(key=cmp_to_key(cmp))

        if strs[0] == "0":
            return "0"

        return "".join(strs)


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        [10, 2],
        [3, 30, 34, 5, 9],
        [0, 0],
        [1],
        [10, 10],
        [0, 1, 0, 9, 3],
    ]

    for nums in test_cases:
        print(f"输入: {nums}, 输出: {solution.largestNumber(nums)}")
