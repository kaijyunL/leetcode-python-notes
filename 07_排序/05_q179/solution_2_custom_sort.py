from functools import cmp_to_key


class Solution:
    def largestNumber(self, nums: list[int]) -> str:
        """
        方法2：自定义排序比较（面试主推）
        时间复杂度：O(n log n * k)
        空间复杂度：O(n * k)
        """
        strings = [str(num) for num in nums]

        def compare(a, b):
            if a + b > b + a:
                return -1
            if a + b < b + a:
                return 1
            return 0

        strings.sort(key=cmp_to_key(compare))

        if strings[0] == "0":
            return "0"

        return "".join(strings)


if __name__ == "__main__":
    solution = Solution()

    assert solution.largestNumber([10, 2]) == "210"
    assert solution.largestNumber([3, 30, 34, 5, 9]) == "9534330"
    assert solution.largestNumber([121, 12]) == "12121"
    assert solution.largestNumber([0, 0, 0]) == "0"
    assert solution.largestNumber([10, 10]) == "1010"
    assert solution.largestNumber([0, 1, 0, 9, 3]) == "93100"

    print("all tests passed")
