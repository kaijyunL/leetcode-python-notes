# 方法1：二维矩阵模拟


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        n = len(s)
        cycle_len = 2 * numRows - 2
        cols = ((n + cycle_len - 1) // cycle_len) * (numRows - 1)
        grid = [[""] * cols for _ in range(numRows)]

        row = 0
        col = 0

        for i, ch in enumerate(s):
            grid[row][col] = ch

            if i % cycle_len < numRows - 1:
                row += 1
            else:
                row -= 1
                col += 1

        ans = []
        for current_row in grid:
            for ch in current_row:
                if ch:
                    ans.append(ch)

        return "".join(ans)


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
