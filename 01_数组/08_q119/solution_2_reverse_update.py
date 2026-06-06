# 方法2：一个数组从后往前更新（面试主推）

from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1] * (rowIndex + 1)

        for i in range(2, rowIndex + 1):
            for j in range(i - 1, 0, -1):
                row[j] = row[j] + row[j - 1]

        return row


if __name__ == "__main__":
    solution = Solution()

    assert solution.getRow(0) == [1]
    assert solution.getRow(1) == [1, 1]
    assert solution.getRow(3) == [1, 3, 3, 1]
    assert solution.getRow(4) == [1, 4, 6, 4, 1]

    print("all tests passed")
