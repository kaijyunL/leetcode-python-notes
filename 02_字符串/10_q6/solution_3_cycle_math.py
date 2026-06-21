# 方法3：周期下标规律


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        n = len(s)
        cycle_len = 2 * numRows - 2
        ans = []

        for row in range(numRows):
            for start in range(0, n, cycle_len):
                vertical_index = start + row
                if vertical_index < n:
                    ans.append(s[vertical_index])

                diagonal_index = start + cycle_len - row
                if 0 < row < numRows - 1 and diagonal_index < n:
                    ans.append(s[diagonal_index])

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
