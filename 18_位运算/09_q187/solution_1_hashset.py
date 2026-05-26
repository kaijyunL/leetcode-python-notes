# 方法1：哈希集合 + 字符串切片


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> list[str]:
        seen = set()
        repeated = set()

        for i in range(len(s) - 9):
            seq = s[i:i + 10]
            if seq in seen:
                repeated.add(seq)
            else:
                seen.add(seq)

        return list(repeated)


if __name__ == "__main__":
    solver = Solution()

    assert set(solver.findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT")) == {
        "AAAAACCCCC",
        "CCCCCAAAAA",
    }
    assert solver.findRepeatedDnaSequences("AAAAAAAAAAAAA") == ["AAAAAAAAAA"]
    assert solver.findRepeatedDnaSequences("ACGT") == []

    print("all tests passed")
