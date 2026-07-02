def is_valid_repeated_replace(s: str) -> bool:
    previous = None

    while s != previous:
        previous = s
        s = s.replace("()", "").replace("[]", "").replace("{}", "")

    return s == ""


if __name__ == "__main__":
    test_cases = [
        ("", True),
        ("()", True),
        ("()[]{}", True),
        ("(]", False),
        ("([)]", False),
        ("{[]}", True),
        ("((", False),
        ("]", False),
        ("([{}])", True),
    ]

    for s, expected in test_cases:
        result = is_valid_repeated_replace(s)
        assert result == expected, f"failed for {s!r}: expected {expected}, got {result}"

    print("all tests passed")
