# 方法1：字符区间合并
class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        char_range: dict[str, list[int]] = {}

        for i, ch in enumerate(s):
            if ch not in char_range:
                char_range[ch] = [i, i]
            else:
                char_range[ch][1] = i

        intervals = sorted(char_range.values())
        ans: list[int] = []

        start, end = intervals[0]
        for left, right in intervals[1:]:
            if left <= end:
                end = max(end, right)
            else:
                ans.append(end - start + 1)
                start, end = left, right

        ans.append(end - start + 1)
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
