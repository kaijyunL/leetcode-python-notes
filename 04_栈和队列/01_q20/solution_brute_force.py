def is_valid_brute_force(s: str) -> bool:
    # 不断替换相邻的匹配对，直到无法替换
    while "()" in s or "[]" in s or "{}" in s:
        s = s.replace("()", "").replace("[]", "").replace("{}", "")
    return s == ""

if __name__ == "__main__":
    test_cases = ["()", "()[]{}", "(]", "([)]", "{[]}"]
    for test in test_cases:
        print(f"输入: {test}, 结果: {is_valid_brute_force(test)}")
