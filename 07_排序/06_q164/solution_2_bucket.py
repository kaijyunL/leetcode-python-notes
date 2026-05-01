class Solution:
    def maximumGap(self, nums: list[int]) -> int:
        """
        解法2：桶排序 + 鸽笼原理 — 面试推荐
        时间复杂度: O(n)
        空间复杂度: O(n)
        """
        if len(nums) < 2:
            return 0

        minVal, maxVal = min(nums), max(nums)
        if minVal == maxVal:
            return 0

        n = len(nums)
        bucketSize = max(1, (maxVal - minVal) // (n - 1))
        bucketCount = (maxVal - minVal) // bucketSize + 1

        bucketMin = [None] * bucketCount
        bucketMax = [None] * bucketCount

        for num in nums:
            idx = (num - minVal) // bucketSize
            if bucketMin[idx] is None:
                bucketMin[idx] = bucketMax[idx] = num
            else:
                bucketMin[idx] = min(bucketMin[idx], num)
                bucketMax[idx] = max(bucketMax[idx], num)

        maxGap = 0
        prevMax = bucketMax[0]

        for i in range(1, bucketCount):
            if bucketMin[i] is None:
                continue
            maxGap = max(maxGap, bucketMin[i] - prevMax)
            prevMax = bucketMax[i]

        return maxGap


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        [3, 6, 9, 1],
        [10],
        [1, 1, 1, 1],
        [1, 10000000],
        [],
        [1, 3, 100],
    ]

    for nums in test_cases:
        print(f"输入: {nums}, 输出: {solution.maximumGap(nums)}")
