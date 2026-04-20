import sys

def simplifyPath(path: str) -> str:
    """
    解法一：手动字符遍历解析
    这种方法不使用 split，通过遍历每个字符来提取目录名。
    """
    n = len(path)
    stack = []
    i = 0
    
    while i < n:
        # 跳过连续的斜杠
        if path[i] == '/':
            i += 1
            continue
        
        # 提取两个斜杠之间的目录名
        start = i
        while i < n and path[i] != '/':
            i += 1
        name = path[start:i]
        
        # 处理提取到的目录名
        if name == '..':
            if stack:
                stack.pop()
        elif name != '.' and name != '':
            stack.append(name)
            
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
