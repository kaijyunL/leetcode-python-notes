class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        i = 0
        n = len(path)

        while i < n:
            while i < n and path[i] == "/":
                i += 1

            start = i
            while i < n and path[i] != "/":
                i += 1

            part = path[start:i]
            if part == "" or part == ".":
                continue
            if part == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(part)

        return "/" + "/".join(stack)


def run_test() -> None:
    solver = Solution()
    test_cases = [
        ("/home/", "/home"),
        ("/../", "/"),
        ("/home//foo/", "/home/foo"),
        ("/a/./b/../../c/", "/c"),
        ("/.../b", "/.../b"),
        ("/../../a", "/a"),
        ("/", "/"),
    ]

    for path, expected in test_cases:
        result = solver.simplifyPath(path)
        assert result == expected, f"failed for {path!r}: expected {expected}, got {result}"


if __name__ == "__main__":
    run_test()
    print("all tests passed")
