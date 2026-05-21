# 方法3：前缀和找最低点
class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        total = 0
        min_prefix = 0
        min_index = -1
        prefix = 0

        for i in range(len(gas)):
            prefix += gas[i] - cost[i]
            total = prefix

            if prefix < min_prefix:
                min_prefix = prefix
                min_index = i

        if total < 0:
            return -1

        return (min_index + 1) % len(gas)


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
