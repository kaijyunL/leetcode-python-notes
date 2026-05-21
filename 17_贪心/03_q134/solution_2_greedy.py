# 方法2：单次遍历贪心
class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        total = 0
        tank = 0
        start = 0

        for i in range(len(gas)):
            diff = gas[i] - cost[i]
            total += diff
            tank += diff

            if tank < 0:
                start = i + 1
                tank = 0

        if total < 0:
            return -1

        return start


if __name__ == "__main__":
    solver = Solution()
    test_cases = [
        ([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]),
        ([2, 3, 4], [3, 4, 3]),
        ([5], [4]),
        ([4], [5]),
        ([3, 1, 1], [1, 2, 2]),
    ]

    for gas, cost in test_cases:
        print(
            f"gas={gas}, cost={cost}, start={solver.canCompleteCircuit(gas, cost)}"
        )
