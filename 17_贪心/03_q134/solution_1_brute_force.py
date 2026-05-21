# 方法1：暴力枚举起点
class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        n = len(gas)

        for start in range(n):
            tank = 0
            success = True

            for step in range(n):
                i = (start + step) % n
                tank += gas[i] - cost[i]
                if tank < 0:
                    success = False
                    break

            if success:
                return start

        return -1


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
