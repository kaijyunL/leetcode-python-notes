# 方法2：一次扫描维护当前片段的最远边界
class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        last = {ch: i for i, ch in enumerate(s)}

        ans = []
        start = 0
        end = 0

        for i, ch in enumerate(s):
            end = max(end, last[ch])

            if i == end:
                ans.append(i - start + 1)
                start = i + 1

        return ans


if __name__ == "__main__":
    solver = Solution()
    test_cases = [
        "ababcbacadefegdehijhklij",
        "eccbbbbdec",
        "abcdef",
        "aaaaa",
    ]

    for s in test_cases:
        print(f"s={s!r}, partitions={solver.partitionLabels(s)}")
