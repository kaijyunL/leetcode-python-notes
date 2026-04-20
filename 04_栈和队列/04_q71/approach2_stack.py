import sys

def simplifyPath(path: str) -> str:
    """
    解法二：最优解 - 字符串分割 + 栈
    面试中最推荐的方法：代码简洁，逻辑清晰。
    """
    # 1. 按斜杠分割路径
    # 例如 "/a/./b/../../c/" -> ['', 'a', '.', 'b', '..', '..', 'c', '']
    parts = path.split("/")
    stack = []
    
    # 2. 遍历每个零件
    for part in parts:
        if part == "..":
            # 遇到 .. ，如果栈不为空则弹出（回退到上一级）
            if stack:
                stack.pop()
        elif part == "." or part == "":
            # 遇到 . 或空字符串（多个斜杠产生），直接忽略
            continue
        else:
            # 遇到正常的目录名，压入栈中
            stack.append(part)
            
    # 3. 将栈中的目录名用 / 拼接，并确保以 / 开头
    return "/" + "/".join(stack)

if __name__ == "__main__":
    # 测试用例
    test_paths = [
        "/home/",
        "/../",
        "/home//foo/",
        "/a/./b/../../c/"
    ]
    
    for p in test_paths:
        print(f"Original: {p:15} Simplified: {simplifyPath(p)}")
