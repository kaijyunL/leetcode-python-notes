from collections import deque


class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        """
        解法2：BFS 队列
        时间复杂度: O(n * 4^n)
        空间复杂度: O(n * 4^n)
        """
        if not digits:
            return []

        phone = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        queue = deque([""])

        for digit in digits:
            for _ in range(len(queue)):
                prefix = queue.popleft()
                for ch in phone[digit]:
                    queue.append(prefix + ch)

        return list(queue)


if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        "23",
        "2",
        "",
        "79",
    ]

    for digits in test_cases:
        print(f"输入: digits={digits!r}, 输出: {solution.letterCombinations(digits)}")
