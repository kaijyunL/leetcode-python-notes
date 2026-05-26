# 方法2：2-bit 滚动编码


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> list[str]:
        if len(s) < 10:
            return []

        value = {"A": 0, "C": 1, "G": 2, "T": 3}
        seen = set()
        repeated = set()
        ans = []

        code = 0
        mask = (1 << 20) - 1

        for i, ch in enumerate(s):
            code = ((code << 2) | value[ch]) & mask

            if i < 9:
                continue

            if code in seen and code not in repeated:
                ans.append(s[i - 9:i + 1])
                repeated.add(code)
            else:
                seen.add(code)

        return ans


if __name__ == "__main__":
    solver = Solution()

    assert set(solver.findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT")) == {
        "AAAAACCCCC",
        "CCCCCAAAAA",
    }
    assert solver.findRepeatedDnaSequences("AAAAAAAAAAAAA") == ["AAAAAAAAAA"]
    assert solver.findRepeatedDnaSequences("ACGT") == []

    print("all tests passed")
