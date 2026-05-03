from collections import Counter


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        """
        解法3：桶排序 — 面试推荐
        时间复杂度: O(n)
        空间复杂度: O(n)
        """
        count = Counter(nums)
        buckets = [[] for _ in range(len(nums) + 1)]

        for num, freq in count.items():
            buckets[freq].append(num)

        ans = []
        for freq in range(len(nums), 0, -1):
            ans.extend(buckets[freq])
            if len(ans) >= k:
                return ans[:k]

        return ans


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        ([1, 1, 1, 2, 2, 3], 2),
        ([1], 1),
        ([4, 1, -1, 2, -1, 2, 3], 2),
        ([3, 3, 3, 3, 2, 2, 1], 2),
    ]

    for nums, k in test_cases:
        print(f"输入: {nums}, k={k}, 输出: {solution.topKFrequent(nums, k)}")
