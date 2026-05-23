# 方法2：数学贪心公式
from collections import Counter


class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        counts = Counter(tasks).values()
        max_count = max(counts)
        max_kinds = sum(1 for count in counts if count == max_count)

        frame_length = (max_count - 1) * (n + 1) + max_kinds
        return max(len(tasks), frame_length)


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
