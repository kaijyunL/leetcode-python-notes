# 方法2：按行模拟（面试主推）


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        rows = [""] * numRows
        row = 0
        direction = 1

        for ch in s:
            rows[row] += ch

            if row == 0:
                direction = 1
            elif row == numRows - 1:
                direction = -1

            row += direction

        return "".join(rows)


def run_case(s: str, num_rows: int, expected: str) -> None:
    actual = Solution().convert(s, num_rows)
    assert actual == expected


if __name__ == "__main__":
    run_case("PAYPALISHIRING", 3, "PAHNAPLSIIGYIR")
    run_case("PAYPALISHIRING", 4, "PINALSIGYAHRPI")
    run_case("A", 1, "A")
    run_case("AB", 1, "AB")
    run_case("ABC", 5, "ABC")

    print("all tests passed")
