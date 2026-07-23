# 方法2：最大堆 + 懒删除

import heapq
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []
        ans = []

        for i, num in enumerate(nums):
            heapq.heappush(heap, (-num, i))

            # 窗口还没形成，不输出答案。
            if i < k - 1:
                continue

            left = i - k + 1

            while heap[0][1] < left:
                heapq.heappop(heap)

            ans.append(-heap[0][0])

        return ans


if __name__ == "__main__":
    solution = Solution()

    assert solution.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3) == [3, 3, 5, 5, 6, 7]
    assert solution.maxSlidingWindow([1], 1) == [1]
    assert solution.maxSlidingWindow([1, -1], 1) == [1, -1]
    assert solution.maxSlidingWindow([9, 11], 2) == [11]
    assert solution.maxSlidingWindow([4, -2], 2) == [4]

    print("all tests passed")
