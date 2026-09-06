from collections import Counter


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        """
        方法3：哈希表 + 频率桶（面试主推）
        时间复杂度：O(n)
        空间复杂度：O(n)
        """
        freq = Counter(nums)
        buckets = [[] for _ in range(len(nums) + 1)]

        for num, count in freq.items():
            buckets[count].append(num)

        ans = []
        for count in range(len(nums), 0, -1):
            ans.extend(buckets[count])
            if len(ans) >= k:
                return ans[:k]

        return ans


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        ([1, 1, 1, 2, 2, 3], 2, {1, 2}),
        ([1], 1, {1}),
        ([4, 1, -1, 2, -1, 2, 3], 2, {-1, 2}),
        ([3, 3, 3, 3, 2, 2, 1], 3, {1, 2, 3}),
    ]

    for nums, k, expected in test_cases:
        assert set(solution.topKFrequent(nums, k)) == expected

    print("all tests passed")
