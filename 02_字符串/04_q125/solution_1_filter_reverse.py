# 方法1：筛选后反转比较
class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered = "".join(ch.lower() for ch in s if ch.isalnum())
        return filtered == filtered[::-1]


def run_case(s: str, expected: bool) -> None:
    actual = Solution().isPalindrome(s)
    assert actual == expected


if __name__ == "__main__":
    run_case("A man, a plan, a canal: Panama", True)
    run_case("race a car", False)
    run_case(" ", True)
    run_case("0P", False)
    run_case("abba", True)

    print("all tests passed")
