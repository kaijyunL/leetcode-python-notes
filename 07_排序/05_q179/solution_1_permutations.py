from itertools import permutations


class Solution:
    def largestNumber(self, nums: list[int]) -> str:
        """
        方法1：全排列枚举
        时间复杂度：O(n! * D)
        空间复杂度：O(n + D)
        """
        ans = ""

        for perm in permutations(nums):
            candidate = "".join(str(x) for x in perm)
            if candidate > ans:
                ans = candidate

        return "0" if ans[0] == "0" else ans


if __name__ == "__main__":
    solution = Solution()

    assert solution.largestNumber([10, 2]) == "210"
    assert solution.largestNumber([3, 30, 34, 5, 9]) == "9534330"
    assert solution.largestNumber([121, 12]) == "12121"
    assert solution.largestNumber([0, 0, 0]) == "0"
    assert solution.largestNumber([10, 10]) == "1010"

    print("all tests passed")
