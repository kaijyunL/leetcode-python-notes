from typing import List


# 方法四：一维压缩动态规划
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = triangle[0][:]

        for row in range(1, len(triangle)):
            dp.append(dp[-1] + triangle[row][row])

            for col in range(row - 1, 0, -1):
                dp[col] = min(dp[col - 1], dp[col]) + triangle[row][col]

            dp[0] += triangle[row][0]

        return min(dp)


if __name__ == "__main__":
    solver = Solution()
    test_cases = [
        [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]],
        [[-10]],
        [[1], [2, 3], [3, 6, 7], [8, 9, 6, 1]],
    ]

    for triangle in test_cases:
        print(f"triangle={triangle}, min_sum={solver.minimumTotal(triangle)}")
