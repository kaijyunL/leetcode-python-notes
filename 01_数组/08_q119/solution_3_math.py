# 方法3：组合数公式

from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1] * (rowIndex + 1)

        for k in range(1, rowIndex + 1):
            row[k] = row[k - 1] * (rowIndex - k + 1) // k

        return row


if __name__ == "__main__":
    solution = Solution()

    assert solution.getRow(0) == [1]
    assert solution.getRow(1) == [1, 1]
    assert solution.getRow(3) == [1, 3, 3, 1]
    assert solution.getRow(4) == [1, 4, 6, 4, 1]

    print("all tests passed")
