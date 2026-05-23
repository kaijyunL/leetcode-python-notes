# 方法1：最大堆模拟调度过程
from collections import Counter, deque
import heapq


class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        counter = Counter(tasks)
        heap = [-count for count in counter.values()]
        heapq.heapify(heap)

        cooldown: deque[tuple[int, int]] = deque()
        time = 0

        while heap or cooldown:
            time += 1

            while cooldown and cooldown[0][0] <= time:
                _, count = cooldown.popleft()
                heapq.heappush(heap, count)

            if heap:
                count = heapq.heappop(heap) + 1
                if count < 0:
                    cooldown.append((time + n + 1, count))

        return time


if __name__ == "__main__":
    solver = Solution()
    test_cases = [
        (["A", "A", "A", "B", "B", "B"], 2),
        (["A", "C", "A", "B", "D", "B"], 1),
        (["A", "A", "A", "B", "B", "B"], 0),
        (["A", "A", "A", "A", "B", "C"], 2),
    ]

    for tasks, n in test_cases:
        print(f"tasks={tasks}, n={n}, time={solver.leastInterval(tasks, n)}")
